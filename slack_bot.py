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

# Spyderbot SlackBot Overview Document: 
# https://docs.google.com/document/d/1N1E67esbNr0NOWolGILMVZsoaNzZkR5SdYvEn0Aec2U/edit?usp=sharing

# Installations required to run this code:
# Install SlackClient (pip install SlackClient)
# Install PIL (pip install Pillow)

# Commands for Spyderbot Slackbot:
#
# To command spyderbot to do something, send a message on slack of the form:
# @spyderbotpython followed by:
# 
#   delete
#   print channel_info
#   print channel_history
#   print this: {your text here}
#   print previous
#   print {any mention of malte. Ex: "messages for malte"}
#   print thread 
#   print thread op
#   print image
# 
#   Example command: @spyderbotpython print this: hello
#           Returns @spyderbotpython: @{user} asked me to print "hello"
#           Which will be printed on the printer attached to spyderbot

x = easeInOutSine

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

# Store the tokens to your machine as environment variables 
oauth_access_token = os.environ.get('oauth_access_token')
print oauth_access_token
bot_user_token = os.environ.get('bot_user_token')
print bot_user_token

printer.println("I'm Alive")
printer.feed(6)

slack_client = SlackClient(bot_user_token)
spyderbot_id = None

websocket.enableTrace(True)

# Global constants 
RTM_READ_DELAY = 1
PRINT_COMMAND = "print"
DELETE_COMMAND = "delete"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
image_types = ["png", "jpg"]

# Parses a command to spyderbot slackbot and returns the message text 
# and channel in which the command was sent
def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == spyderbot_id:
                return message, event["channel"]
        elif "comment" in event and "type" in event:
            if event["type"] == "message":
                user_id, message = parse_direct_mention(event["comment"]["comment"])
                if user_id == spyderbot_id:
                    return message, event["channel"]

    return None, None

# Parses a message for a mention of the username of the slackbot
def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    if matches:
        return (matches.group(1), matches.group(2).strip())
    else:
        return (None, None)

# Creates a dictionary that maps user ids to usernames
# Ex: {U1234567 : JaneDoe} represents the username @JaneDoe belonging to user U1234567
# This dictionary is used to efficiently convert user ids to usernames 
# in message texts
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

# Creates a map of emoji names to the number of reactions that emoji 
# recieved for a particular message
# Ex. {smile : 3} represents the reaction smile being chosen by 3 users
def make_emoji_map(emoji_map, message):

    if "reactions" in message:
        for r in message["reactions"]:
            emoji_map[r['name']] = r["count"]

    return emoji_map

# Prints the channel of the channel that the message command was sent in
# The channel info for the channel is accessed by an api call to the slack api.
# and then parsed and formatted into a a string containing the channel name, creator,
# topic, purpose, and members.
# For more info: https://api.slack.com/methods/channels.info
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

# Returns all the messages in the channel as a list of message objects
# For more info: https://api.slack.com/methods/channels.history
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

# Returns a message that is the same as the passed in [message] but 
# has replaced every instance of an user id with the corresponding username
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

# Prints the messages immediately preceding the message that was sent to
# command Spyderbot to print previous. 
# Ex. 
# user1 : message 1
# user1 : @spyderbotpython print previous
# Returns the response: @user1 asked me to print @user1 saying "message 1"
#
# If the previous message is an image, the image will be printed
def print_previous_message(messages, users_map):

    if messages == None:
        return "An error occured, sorry!"

    #The command was part of a comment on a file (currently only images are implemented)
    if "comment" in messages[0]:
        file_id = messages[0]["file"]["id"]
        file_info = slack_client.api_call(
          "files.info",
          token=oauth_access_token,
          file=file_id,
        )
        comments = list(reversed(file_info["comments"]))
        print comments
        previous_message = comments[1]
        previous_message_text = comments[1]["comment"]
        requestor = comments[0]["user"]
    else:
        #the requestor is the user who asked to "print previous"
        #always a user never a bot
        requestor = messages[0]["user"]

        #The "previous" message is located at index 1 because the message at index 0 asks to print
        previous_message = messages[1]
        previous_message_text = messages[1]["text"]

    emoji_map = {}
    emoji_map = make_emoji_map(emoji_map, previous_message)


    if "file" in previous_message:
        print previous_message
        if previous_message["file"]["filetype"] in image_types:
            url = previous_message["file"]["thumb_360"]
            print_image(url)

    if "user" in previous_message:
        user_name = users_map[previous_message["user"]]

    if "bot_id" in previous_message:
        user_name = previous_message["username"]

    message_parsed = parse_message(previous_message_text, users_map)

    return ("@" + users_map[requestor] + " asked me to print @" + user_name + " saying \"" + message_parsed + "\"", emoji_map)

# Prints all the messages in the channel that were retrived by the api call 
# to the slack api for messages.
# For more info: https://api.slack.com/methods/channels.history
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

# Prints the message text following the command "print this:"
# Ex. user : @spyderbotpython print this: hello
# Returns the response: @user asked me to print "hello"
def print_latest(curr, messages, users_map):

    message = messages[0]

    #Is a comment on a file (only images implemented currently)
    if "comment" in message:
        requestor = message["comment"]["user"]
    else:
        requestor = message["user"]

    response = "@" + users_map[requestor] + " asked me to print \"" + curr + "\""

    return response

# Prints all the messages in a channel that mention Malte from the past day.
# In the command, any mention of malte will trigger this command.
# Ex: @user : @spyderbotpython print messages for malte
# All messages in the last 24 hours containing the word malte will be printed.
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

# Prints the top, or original post (op) of a thread
# If the original post is an image, the image will be printed
def print_thread_op(channel, messages, users_map):

    #Currently only works when commenting on image files
    if "comment" in messages[0]:
        # last_comment = messages[0]["ts"]
        last_user = messages[0]["comment"]["user"]
        url = messages[0]["file"]["thumb_360"]
        print_image(url)
        return ("@" + users_map[last_user] + " asked me to print the file they commented on.", {}) 
    else:
        last_comment = messages[0]["ts"]
        last_user = messages[0]["user"]

    for m in messages:
        if "replies" in m:
            for r in m["replies"]:
                if r["ts"] == last_comment and r["user"] == last_user:
                    # print m
                    emoji_map = {}
                    emoji_map = make_emoji_map(emoji_map, m)
                    message_parsed = parse_message(m["text"], users_map)
                    if "user" in m:
                        return ("@" + users_map[last_user] + " asked me to print the op message by @" + users_map[m["user"]] + ": " + message_parsed, emoji_map)
                    if "bot_id" in m:
                        return ("@" + users_map[last_user] + " asked me to print the op message by @" + m["username"] + ": " + message_parsed, emoji_map)

    return "An error occured, are you sure you're replying to thread?"

# Prints an entire thread including the original post and all comments that follow
# Will work for threads whose op is an image
def print_thread(channel, messages, users_map):

    response = ""

    if "comment" in messages[0]:
        requestor = messages[0]["comment"]["user"]
        file_id = messages[0]["file"]["id"]
        url = messages[0]["file"]["thumb_360"]
        print_image(url)
        file_info = slack_client.api_call(
          "files.info",
          token=oauth_access_token,
          file=file_id,
        )
        comments = file_info["comments"]

        for c in comments:
            parsed_message = parse_message(c["comment"], users_map)
            response += "@" + users_map[c["user"]] + ": " + parsed_message + "\n"

        return response

    elif "thread_ts" in messages[0]:

        thread_ts = messages[0]["thread_ts"]

        for m in messages:
            if thread_ts == m["ts"]:
                op = m
                replies_list = m["replies"]

        parsed_op_message = parse_message(op["text"], users_map)

        if "user" in op:
            user = users_map[op["user"]]
        if "username" in op:
            user = op["username"]

        response += "@" + user + ": " + parsed_op_message + "\n"

        for r in replies_list:
            r_user = r["user"]
            r_ts = r["ts"]
            for m in messages:
                if "user" in m and m["user"] == r_user and m["ts"] == r_ts:
                    parsed_message = parse_message(m["text"], users_map)
                    response += "@" + users_map[m["user"]] + ": " + parsed_message + "\n"

        return response
    else:
        return "An error occured, are you sure you're replying to thread?"

    return "An error occured, sorry!"

# Prints the image that is being commented on. This command will only work
# if it is a used as a comment on an image file 
def print_image_from_comment(channel, messages):

    if "comment" in messages[0]:
        url = messages[0]["file"]["thumb_360"]
        print_image(url)
    else:
        return "An error occured, are you sure you're commenting on a file?"

# Deletes massages that were sent to a channel by Spyderbot
# Use this function to clean up the channel if needed by deleting 
# old messages from Spyderbot
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

# Function that executes the printing action of the response from
# Spyderbot to the physical printer 
def execute_print(channel, response):

    try:
        printer.println(response)
        printer.feed(6)
    except:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text="An error occured, could not print to spyderbot."
        )

# Prints an image given a valid image url 
# Function that executes the printing action of an image given 
# a valid image url  from Spyderbot to the physical printer.
# 
# If the image cannot be printed, the exception will be printed to the 
# command line and an error message will be printed instead.
def print_image(url):

    try:
        bearer = "Bearer " + oauth_access_token
        headers = {"Authorization":bearer}

        response = requests.get(url, headers=headers, stream=True)
        img = StringIO(response.content)
        resized_image = Image.open(img)

        print "image ok"
        printer.printImage(resized_image)
        printer.feed(1)
    except Exception as e:
        print(e)
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text="An error occured, could not print image to spyderbot."
        )

# Function that executes the printing action of emoji reactions of a message
# from Spyderbot to the physical printer 
def print_emojis(channel, emoji_map):

    emojis = slack_client.api_call("emoji.list", token=oauth_access_token)
    emojis = emojis["emoji"]

    for e in emoji_map:
        for i in range(0, emoji_map[e]):
            if e in emojis:
                print_image(emojis[e])

# Function that handles the flow of command from the message command to the
# corresponding function that can execute that command
#
# Each of the prior functions called in this function returns a response 
# and sometimes an emoji map which are returned by this function. If no
# either the response or emoji map are missing the defaults for those 
# will be returned
def handle_print_command(command, channel, users_map):
    command_split = command.split()
    command_split = [s.lower() for s in command_split]

    emoji_map = {}

    if len(command_split) > 1:
        if command_split[1] == "previous":
            messages = get_messages(channel)
            response, emoji_map = print_previous_message(messages, users_map)
        elif command_split[1] == "channel_info":
            response = print_channel_info(channel, users_map)
        elif command_split[1] == "channel_history":
            messages = get_messages(channel)
            response = print_channel_history(messages, users_map)
        elif command_split[1] == "this:":
            messages = get_messages(channel)
            response = print_latest(" ".join(command_split[2:]), messages, users_map)
        #command example: "Print messages for malte"
        elif "malte" in command_split:
            response = print_malte_messages(channel, users_map)
        elif command_split[1] == "op":
            messages = get_messages(channel)
            response, emoji_map = print_thread_op(channel, messages, users_map)
        elif command_split[1] == "thread":
            messages = get_messages(channel)
            response = print_thread(channel, messages, users_map)
        elif command_split[1] == "image":
            messages = get_messages(channel)
            response = print_image_from_comment(channel, messages)
        else:
            response = "That print command does not exist currently. Try previous, channel_info, or channel_history."

    else:
        response = "You need to specify what to print. Try previous, channel_info, or channel_history."

    return response, emoji_map

# Function that handles the flow of command from a message command to 
# the corresponding type of command mentioned in the message
# This function also prints the response to the physical printer and sends
# the response as a message to the channel from SPyderbot
def handle_command(command, channel, users_map):

    default_response = "Something went wrong, check exception traceback."

    response = None
    if command.startswith(PRINT_COMMAND):
        response, emoji_map = handle_print_command(command, channel, users_map)
    if command.startswith(DELETE_COMMAND):
        emoji_map = None
        messages = get_messages(channel)
        response = handle_delete_command(messages)

    execute_print(channel, response)

    if emoji_map is not None and len(emoji_map) > 0:
        print_emojis(channel, emoji_map)

    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

# Function to start flow of command to Spyderbot SlackBot
if __name__ == "__main__":
    print(slack_client.rtm_connect)
    if slack_client.rtm_connect(with_team_state = False):

        print("alert")
        easingMultiple(motionforward, .75)
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