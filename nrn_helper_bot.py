# Nicole-Rene's Helper Bot Slack App
# Created by: Nicole-Rene Newcomb
# Newest Version Date: 07/30/2023
# Description: This Slack App Bot acts as a helper and assistant.

import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Setting logging details to output messages to log file
logging.basicConfig(format='Logged at %(asctime)s %(message)s:', filename='nrn_helper_bot.log',
                    encoding='utf-8', level=logging.DEBUG)
logging.debug(' - Debug - ')
logging.info(' - Info - ')
logging.warning(' - Warning - ')
logging.error(' - Error - ')

