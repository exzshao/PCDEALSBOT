import os
from dotenv import load_dotenv
load_dotenv('.env')

discordToken = os.getenv('DISCORDTOKEN')
redditClient = os.getenv('REDDITCLIENT')
redditSecret = os.getenv('REDDITSECRET')

redditUser = os.getenv('REDDITUSER')
redditPass = os.getenv('REDDITPASS')