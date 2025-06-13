import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
COMMAND_PREFIX = '!'
MUSIC_FOLDER = 'music'

# Bot settings
MAX_VOLUME = 100
DEFAULT_VOLUME = 50

# Discord intents
# Set to False to avoid privileged intents requirement
# If you need message content intent, enable it in Discord Developer Portal first
INTENTS_MESSAGE_CONTENT = True
INTENTS_VOICE_STATES = True
