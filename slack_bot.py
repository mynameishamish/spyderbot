import os
import time
import re
from slackclient import SlackClient
from Adafruit_Thermal import *
import urllib, json

# import time
# import math
# import numpy
#
# from easing import *
# from motions import *
#
# x = easeInOutSine
#
# printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

#READ ME:
#Install SlackClient to run this code (pip install SlackClient)

#TODO:
#Channel History: Convert user ids in text to usernames
#Print attachments and images - Have access to image permalink and url

oauth_access_token = os.environ.get('oauth_access_token')
print oauth_access_token
bot_user_token = os.environ.get('bot_user_token')
print bot_user_token

slack_client = SlackClient(bot_user_token)
spyderbot_id = None

RTM_READ_DELAY = 1
PRINT_COMMAND = "print"
DELETE_COMMAND = "delete"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == spyderbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    if matches:
        return (matches.group(1), matches.group(2).strip())
    else:
        return (None, None)

def get_user_info(user):
    user_info = slack_client.api_call(
      "users.info",
      token=oauth_access_token,
      user=user
    )

    if "error" in user_info:
        print "the users.info error was: " + str(user_info["error"])
        return None

    return user_info

def get_bot_info(bot):

    bot_info = slack_client.api_call(
      "users.info",
      token=oauth_access_token,
      bot=bot
    )

    if "error" in bots_info:
        print "the bots.info error was: " + str(user_info["error"])
        return None

    return bot_info


def print_channel_info(channel):
    #channels.info will only work in a channel, not a direct chat
    channel_info = slack_client.api_call(
      "channels.info",
      channel=channel
    )

    if "error" in channel_info:
        print "the channels.info error was: " + str(channel_info["error"])
        return "An error occured, sorry!"

    name = channel_info["channel"]["name"]
    creator = channel_info["channel"]["creator"]
    topic = channel_info["channel"]["topic"]["value"]
    purpose = channel_info["channel"]["purpose"]["value"]
    members = channel_info["channel"]["members"]
    members_user_names = []

    for mem in members:
        if mem[0] == "U":
            user_info = get_user_info(mem)
            if user_info == None:
                return "An error occured getting user info, sorry!"
            user_name = user_info["user"]["real_name"]
        elif mem[0] == "B":
            bot_info = get_bot_info(mem)
            if bot_info == None:
                return "An error occured getting bot info, sorry!"
            user_name = bots_info["bot"]["name"]

        members_user_names.append(user_name)

    creator_user_info = get_user_info(creator)
    if creator_user_info == None:
            return "An error occured getting user info, sorry!"

    info = "The channel is called #" + name + " and was created by @" + creator_user_info["user"]["real_name"]

    if topic == "":
        info += ". There is no topic set for the channel"
    else:
        info += ". The topic of the channel is \"" + topic + "\""

    if purpose == "":
        info += ". There is no purpose set for the channel. "
    else:
        info += ". The purpose of the channel is \"" + purpose + "\"."

    for mem in members_user_names[:-1]:
        info += " @" + mem + ", "
    info += " and @" + members_user_names[-1] +" are members of the channel."

    return info

def get_messages(channel):
    channel_history = slack_client.api_call(
      "channels.history",
      token=oauth_access_token,
      channel=channel
    )

    if "error" in channel_history:
        print "the channels.history error was: " + str(channel_history["error"])
        return None

    messages = channel_history["messages"]

    return messages


def print_previous_message(messages):

    if messages == None:
        return "An error occured, sorry!"

    #the requestor is the user who asked to "print previous"
    #always a user never a bot
    requestor = messages[0]["user"]
    requestor_user_info = get_user_info(requestor)

    #The "previous" message is located at index 1 because the message at index 0 asks to print
    previous_message = messages[1]
    previous_message_text = messages[1]["text"]

    if "file" in previous_message:
        previous_message_file_permalink = previous_message["file"]["permalink"]
        previous_message_file_url = previous_message["file"]["url_private"]

    if "user" in previous_message:
        user = previous_message["user"]
        user_info = get_user_info(user)
        if user_info == None:
            return "An error occured getting user info, sorry!"
        user = user_info["user"]["real_name"]

    if "bot_id" in previous_message:
        user = previous_message["username"]

    if requestor_user_info == None:
        return "An error occured getting user info, sorry!"


    return "@" + requestor_user_info["user"]["real_name"] + " asked me to print @" + user + " saying \"" + previous_message_text + "\""

def print_channel_history(messages):

    if messages == None:
        return "An error occured, sorry!"

    response = ""

    for m in reversed(messages):
        if "user" in m:
            user_info = get_user_info(m["user"])

            if user_info == None:
                return "An error occured getting user info, sorry!"

            user_name = user_info["user"]["real_name"]
            response += "@" + user_name + ": " + m["text"] + "\n"
        if "bot_id" in m:
            response += "@" + m["username"] + ": " + m["text"] + "\n"

    return response

def handle_print_command(command, channel):
    command_split = command.split()

    if len(command_split) > 1:
        if command_split[1] == "previous":
            messages = get_messages(channel)
            response = print_previous_message(messages)
        if command_split[1] == "channel_info":
            response = print_channel_info(channel)
        if command_split[1] == "channel_history":
            messages = get_messages(channel)
            response = print_channel_history(messages)
    else:
        response = "You need to specify what to print. Try previous, channel_info, or channel_history"

    return response

#Currently checking for bot username - change this to use bot_id
def handle_delete_command(messages):

    ts_list = []

    for m in messages:
        if "username" in m and m["username"] == "Spyderbot-python":
            if "ts" in m:
                ts_list.append(m["ts"])

    for ts in ts_list:
        slack_client.api_call(
          "chat.delete",
          channel=channel,
          ts=ts
        )

    return "Deleted my messages."

def execute_print(channel, response):

    #First argument depends on type of system: Linux, Windows, etc.

    try:
        printer.println(response)
        printer.feed(6)
    except:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text="An error occured, could not print to spyderbot."
        )


#X asked me to print Y saying ....
#Printing images and attachements

def handle_command(command, channel):

    default_response = "Something went wrong, check exception traceback."

    response = None
    if command.startswith(PRINT_COMMAND):
        response = handle_print_command(command, channel)
    if command.startswith(DELETE_COMMAND):
        messages = get_messages(channel)
        response = handle_delete_command(messages)

    execute_print(channel, response)

    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state = False):

        # print("alert")
        # easingMultiple(motionalert, .75)
        # time.sleep(2)

        print("Spyder Bot connected and running!")

        spyderbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
