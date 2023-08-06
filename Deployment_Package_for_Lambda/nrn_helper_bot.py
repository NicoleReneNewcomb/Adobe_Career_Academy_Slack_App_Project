""" Nicole-Rene's Helper Bot Slack App
    Created by: Nicole-Rene Newcomb
    Newest Version Date: 07/30/2023
    Description: This Slack App Bot acts as a helper and assistant.
"""


import logging
import sys
import os
import random
import json
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

# path to access python folder within lambda function folder structure
python_folder = os.path.join(os.path.dirname(__file__), 'python')
sys.path.append(python_folder)
import requests

# Setting logging details to output messages to log file
logging.basicConfig(format='Logged at %(asctime)s: #### %(message)s ####',
                    filename='nrn_helper_bot.log', encoding='utf-8', level=logging.INFO)
logging.debug('INFO MODE')

# Setting up environmental variables
SLACK_BOT_TOKEN = os.environ["NRN_Helper_Bot_User_OAth_Token"]
SLACK_SIGNING_SECRET = os.environ["NRN_Helper_Bot_Signing_Secret"]

# Create instance of slack app using bot socket token
nrn_helper_bot = App(signing_secret=SLACK_SIGNING_SECRET, token=SLACK_BOT_TOKEN)

# Create list of cute animal photos
cute_animals_photos =\
['https://images.pexels.com/photos/39317/chihuahua-dog-puppy-cute-39317.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/157465/pexels-photo-157465.jpeg?auto=compress&w=320&h=320', 
'https://images.pexels.com/photos/314865/pexels-photo-314865.jpeg?auto=compress&w=320&h=320',
'https://images.pexels.com/photos/2538270/pexels-photo-2538270.jpeg?auto=compress&w=320&h=320',
'https://images.pexels.com/photos/5033770/pexels-photo-5033770.jpegauto=compress&w=320&h=320',
'https://images.pexels.com/photos/45170/kittens-cat-cat-puppy-rush-45170.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/2835623/pexels-photo-2835623.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/17189473/pexels-photo-17189473.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/16716103/pexels-photo-16716103.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/10386196/pexels-photo-10386196.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/5187249/pexels-photo-5187249.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/7938587/pexels-photo-7938587.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/15773227/pexels-photo-15773227.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/6959442/pexels-photo-6959442.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/6897445/pexels-photo-6897445.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/4147986/pexels-photo-4147986.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/14000649/pexels-photo-14000649.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/10459118/pexels-photo-10459118.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/4190869/pexels-photo-4190869.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/7324407/pexels-photo-7324407.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/9809416/pexels-photo-9809416.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/3610168/pexels-photo-3610168.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/730537/pexels-photo-730537.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/9759731/pexels-photo-9759731.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/5910875/pexels-photo-5910875.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/7293362/pexels-photo-7293362.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/17744112/pexels-photo-17744112.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/15557809/pexels-photo-15557809.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/792416/pexels-photo-792416.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/674318/pexels-photo-674318.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/460775/pexels-photo-460775.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/106685/pexels-photo-106685.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/50577/hedgehog-animal-baby-cute-50577.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/1643456/pexels-photo-1643456.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/2189599/pexels-photo-2189599.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/905248/pexels-photo-905248.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/1692984/pexels-photo-1692984.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/1123771/pexels-photo-1123771.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/3839696/pexels-photo-3839696.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/819372/pexels-photo-819372.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/3661927/pexels-photo-3661927.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/326929/pexels-photo-326929.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/332153/pexels-photo-332153.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/1322599/pexels-photo-1322599.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/15624135/pexels-photo-15624135.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/260143/pexels-photo-260143.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/271932/pexels-photo-271932.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/7101144/pexels-photo-7101144.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/5263832/pexels-photo-5263832.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/356547/pexels-photo-356547.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/1458911/pexels-photo-1458911.jpeg?auto=compress&h=320',
'https://images.pexels.com/photos/2301173/pexels-photo-2301173.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/133468/pexels-photo-133468.jpeg?auto=compress&w=320',
'https://images.pexels.com/photos/6131004/pexels-photo-6131004.jpeg?auto=compress&h=320']

#Function to handle Slack to AWS Lambda requests
def lambda_handler(event, context):
    """handles Slack events sent to lambda"""
    body = event["body"]
    payload = json.loads(body.get("payload", "{}"))
    response = nrn_helper_bot.dispatch(payload)

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

# Download and cache images to reduce latency
def download_and_cache_images():
    """downloads/caches images to reduce latency"""
    cached_images = []
    for url in cute_animals_photos:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Save the image locally in a cache folder
                image_filename = os.path.basename(url)
                cache_path = f"cache/{image_filename}"
                with open(cache_path, "wb") as new_file:
                    new_file.write(response.content)
                cached_images.append(cache_path)
        except IOError as err:
            print(f"Error downloading {url}: {err}")
    return cached_images


######### Event handlers section #########

# Event handler for when Nicole-Rene's Helper Bot is mentioned by name
@nrn_helper_bot.event("app_mention")
def mention_handler(event, say):
    """function to handle app_mention event"""
    user = event['user']
    bot_help_txt = "Please type \"bot help\" to see available commands."
    bot_message = f"Hello there, <@{user}>! How can I help you? {bot_help_txt}"
    say(text=bot_message)

# Event handler to listen for phrase "Bot Help" in messages
@nrn_helper_bot.message("bot help")
def bot_help(say):
    """responding to "bot help" message"""
    option1 = "cute animals, "
    option2 = ":wave:"
    bot_message = f"Here are some options: {option1}{option2}"
    say(text=bot_message)

# Event handler to listen for the ":wave:" emoji in messages
@nrn_helper_bot.message(":wave:")
def wave(message, say):
    """responding to a wave emoji message"""
    user = message['user']
    say(text=f"Hi there, <@{user}>!")

# Event handler to listen for phrase "cute animals" in messages
@nrn_helper_bot.message("cute animals")
def cute_animals(ack, say):
    """responding to a wave emoji message"""
    ack()
    random_cute_animal = random.choice(cute_animals_photos)
    # say("Here's a cute animal for you!")

    say(
        {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Here's a cute animal photo for you:",
                    },
                },
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Cute Animal",
                    },
                    "image_url": random_cute_animal,
                    "alt_text": "Cute Animal",
                },
            ]
        }
    )

###### End of event handlers section ######
