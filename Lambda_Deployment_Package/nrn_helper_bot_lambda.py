""" Nicole-Rene's Helper Bot Slack App for Lambda
    Created by: Nicole-Rene Newcomb
    Newest Version Date: 08/01/2023
    Description: This Slack App Bot operates via AWS Lambda
"""

import logging
import random
from cute_animal_photos import cute_animals_photos
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

# Setting logging details and formatting message output
SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

# Parameter provides rapid response to requests (avoids timeout when using FaaS)
nrn_helper_bot = App(process_before_response=True)

# Main handler for incoming requests to AWS Lambda function from Slack
def lambda_handler(event, context):
    """handles incoming requests from Slack to AWS Lambda function"""
    # Create instance of bot
    slack_handler = SlackRequestHandler(app=nrn_helper_bot)
    # Route request to proper handler
    return slack_handler.handle(event, context)


######### Event/command handlers section #########

# Event handler for when Nicole-Rene's Helper Bot is mentioned by name
@nrn_helper_bot.event("app_mention")
def mention_handler(body, event, say, ack, logger):
    """handles app_mention events when @<botname> referenced"""
    ack()
    logger.info(body)
    user = event['user']
    bot_help_txt = "Please enter command /help to see available commands."
    bot_message = f"Hello there, <@{user}>! How can I help you? {bot_help_txt}"
    say(text=bot_message)

# Event handler to listen for the ":wave:" emoji message
@nrn_helper_bot.message(":wave:")
def wave(message, say, ack):
    """handles a wave emoji message"""
    ack()
    user = message['user']
    say(text=f"And a :wave: to you too, <@{user}>!")

# Response to general message events
@nrn_helper_bot.event("message")
def message_response(ack, say):
    """handles general message events from channel"""
    #Acknowledges receipt of event, but no content sent to channel
    ack()
    say("Message Received.")

# Command handler to respond to /help command
@nrn_helper_bot.command("/help")
def help_command(ack, say):
    """handles /help command"""
    ack()
    option1 = "\n/cuteanimals - displays a random photo of cute animals"
    option2 = "\n/inspiration - displays a random inspirational quote"
    option3 = "\n mention :wave: in message - bot waves back to you"

    bot_message = f"Here are some options: {option1}{option2}{option3}"
    say(text=bot_message)

# Event handler to respond to /cuteanimals command
@nrn_helper_bot.command("/cuteanimals")
def cute_animals(ack, say):
    """responding to a wave emoji message"""
    ack()
    random_cute_animal = random.choice(cute_animals_photos)

    # Sends both a text message and an image url back to Slack
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

###### End of event/command handlers section ######
