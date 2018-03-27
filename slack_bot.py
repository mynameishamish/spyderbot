from Adafruit_Thermal import *
import datetime
from cStringIO import StringIO
import io
import os
from oauthlib.common import add_params_to_uri
from PIL import Image
import re
import requests
from slackclient import SlackClient
import time
import urllib, json
import urllib2 as urllib2
import websocket

import time
import math
import numpy

from easing import *
from motions import *

x = easeInOutSine

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)


#READ ME:
#Install SlackClient to run this code (pip install SlackClient)
#Install PIL (pip install Pillow)
#Install OauthLib (pip install oauthlib)

#TODO:
#Print attachments and images - DONE (maybe)
#Print malte's messages - DONE
#Investigate threads - In process

oauth_access_token = os.environ.get('oauth_access_token')
print oauth_access_token
bot_user_token = os.environ.get('bot_user_token')
print bot_user_token

printer.println("I'm Alive")
printer.feed(6)

slack_client = SlackClient(bot_user_token)
spyderbot_id = None

websocket.enableTrace(True)

RTM_READ_DELAY = 1
PRINT_COMMAND = "print"
DELETE_COMMAND = "delete"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
image_types = ["png", "jpg"]

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

def user_id_map():
    users_list = slack_client.api_call(
      "users.list",
      token=oauth_access_token,
    )

    if "error" in users_list:
        print "the users.list error was: " + str(users_list["error"])
        return None

    users_map = {}
    for user in users_list["members"]:
        if user["is_bot"]:
            users_map[user["id"]] = user["profile"]["real_name"]
        else:
            users_map[user["id"]] = user["profile"]["display_name"]

    return users_map


def print_channel_info(channel, users_map):
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
        members_user_names.append(users_map[mem])

    info = "The channel is called #" + name + " and was created by @" + users_map[creator]

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


def print_image(message):

    url = message["file"]["url_private"]

    #must use url_private
    # url = 'https://files.slack.com/files-pri/T380FS421-F9PAQ484W/image.png'

    try:
        bearer = "Bearer " + oauth_access_token
        headers = {"Authorization":bearer}

        response = requests.get(url, headers=headers, stream=True)
        img = StringIO(response.content)
        resized_image = Image.open(img)

        print "image ok"
        printer.printImage(resized_image)
        printer.feed(6)
    except Exception as e:
        print(e)
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text="An error occured, could not print image to spyderbot."
        )


def parse_message(message, users_map):

    start_idx = 0
    new_message = ""

    user_ids = [m.start() for m in re.finditer('<@', message)]

    for id_pos in user_ids:

        id_end = message.find(">", id_pos)

        user_name = users_map[message[id_pos+2:id_end]]

        new_message += message[start_idx:id_pos] + " @" + user_name
        start_idx = id_end+1

    return new_message + message[start_idx:]


def print_previous_message(messages, users_map):

    if messages == None:
        return "An error occured, sorry!"

    #the requestor is the user who asked to "print previous"
    #always a user never a bot
    requestor = messages[0]["user"]

    #The "previous" message is located at index 1 because the message at index 0 asks to print
    previous_message = messages[1]
    previous_message_text = messages[1]["text"]

    if "file" in previous_message:
        print previous_message
        if previous_message["file"]["filetype"] in image_types:
            print_image(previous_message)

    if "user" in previous_message:
        user_name = users_map[previous_message["user"]]

    if "bot_id" in previous_message:
        user_name = previous_message["username"]

    message_parsed = parse_message(previous_message_text, users_map)

    return "@" + users_map[requestor] + " asked me to print @" + user_name + " saying \"" + message_parsed + "\""

def print_channel_history(messages, users_map):

    if messages == None:
        return "An error occured, sorry!"

    response = ""

    for m in reversed(messages):

        parsed_message = parse_message(m["text"], users_map)

        if "user" in m:
            response += "@" + users_map[m["user"]] + ": " + parsed_message + "\n"
        if "bot_id" in m:
            response += "@" + m["username"] + ": " + parsed_message + "\n"

    return response


def print_latest(curr, messages, users_map):

    message = messages[0]

    if "file" in message:
        if message["file"]["filetype"] in image_types:
            print_image(message)

    requestor = message["user"]

    response = "@" + users_map[requestor] + " asked me to print \"" + curr + "\""

    return response


def print_malte_messages(channel, users_map):

    yesterday = datetime.date.today() - datetime.timedelta(1)

    timestamp = time.mktime(yesterday.timetuple())

    channel_history = slack_client.api_call(
      "channels.history",
      token=oauth_access_token,
      channel=channel,
      oldest=timestamp
    )

    if "error" in channel_history:
        print "the channels.history error was: " + str(channel_history["error"])
        return None

    response = ""
    has_messages = False
    messages = channel_history["messages"]

    for m in reversed(messages):
        if "malte" in m["text"]:
            has_messages = True
            parsed_message = parse_message(m["text"], users_map)

            if "user" in m:
                response += "@" + users_map[m["user"]] + ": " + parsed_message + "\n"
            if "bot_id" in m:
                response += "@" + m["username"] + ": " + parsed_message + "\n"

    if has_messages:
        return response
    else:
        return "No messages for Malte today."


def handle_print_command(command, channel, users_map):
    command_split = command.split()
    command_split = [s.lower() for s in command_split]


    #### DELETE ####
    # print "here"
    # messages = get_messages(channel)
    # for m in reversed(messages):
    #     print m

    if len(command_split) > 1:
        if command_split[1] == "previous":
            messages = get_messages(channel)
            response = print_previous_message(messages, users_map)
        if command_split[1] == "channel_info":
            response = print_channel_info(channel, users_map)
        if command_split[1] == "channel_history":
            messages = get_messages(channel)
            response = print_channel_history(messages, users_map)
        if command_split[1] == "this:":
            #currently pulling all messages to get the latest user - can do better
            messages = get_messages(channel)
            response = print_latest(" ".join(command_split[2:]), messages, users_map)
        #command: "Print messages for malte"
        if "malte" in command_split:
            response = print_malte_messages(channel, users_map)
    else:
        response = "You need to specify what to print. Try previous, channel_info, or channel_history"

    return response

#Currently checking for bot username - change this to use bot_id
def handle_delete_command(messages):

    ts_list = []

    for m in messages:
        if "username" in m and m["username"] == "Spyderbot":
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

def handle_command(command, channel, users_map):

    default_response = "Something went wrong, check exception traceback."

    response = None
    if command.startswith(PRINT_COMMAND):
        response = handle_print_command(command, channel, users_map)
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
    print(slack_client.rtm_connect)
    if slack_client.rtm_connect(with_team_state = False):

        print("alert")
        easingMultiple(motionalert, .75)
        printer.println("Spyder Bot connected and running!")
        printer.feed(6)     
        time.sleep(1)

        print("Spyder Bot connected and running!")

        spyderbot_id = slack_client.api_call("auth.test")["user_id"]

        users_map = user_id_map()
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel, users_map)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
