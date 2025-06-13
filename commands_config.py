# MuskaBot Commands Configuration
# Customize all command names, descriptions, and messages here

# =============================================================================
# BOT SETTINGS
# =============================================================================

# Command prefix (what users type before commands)
COMMAND_PREFIX = '!'  # Change this to ? or any other character you want

# =============================================================================
# COMMAND SETTINGS
# =============================================================================

# Command names (what users type after the prefix)
COMMANDS = {
    'join': 'm_join',           # !join (change to 'mjoin' for !mjoin)
    'leave': 'm_leave',         # !leave  
    'play': 'm_play',           # !play
    'pause': 'm_pause',         # !pause
    'resume': 'm_resume',       # !resume
    'stop': 'm_stop',           # !stop
    'volume': 'm_volume',       # !volume
    'list': 'm_list',           # !list
    'random': 'm_random',       # !random
    'current': 'm_current',     # !current
    'help': 'm_help_music',     # !help_music
}

# =============================================================================
# RESPONSE MESSAGES
# =============================================================================

MESSAGES = {
    # Success messages
    'joined_channel': "🎵 Joined **{channel_name}**! Ready to play music!",
    'left_channel': "👋 Left the voice channel! See you later!",
    'now_playing': "🎶 Now playing: **{track_name}**",
    'paused': "⏸️ Paused playback!",
    'resumed': "▶️ Resumed playback!",
    'stopped': "⏹️ Stopped playback!",
    'currently_playing': "🎵 Currently playing: **{track_name}**",
    
    # Error messages
    'not_in_voice': "❌ You need to be in a voice channel to use this command!",
    'failed_to_join': "❌ Failed to join voice channel!",
    'song_not_found': "❌ Could not find song: **{song_name}**",
    'nothing_playing': "❌ Nothing is currently playing!",
    'nothing_paused': "❌ Nothing is paused!",
    'not_in_channel': "❌ I'm not in a voice channel!",
    'no_songs_found': "❌ No MP3 files found in the music folder!",
    'specify_song': "❌ Please specify a song name or use `{prefix}list` to see available songs.",
    'volume_range': "❌ Volume must be between 0 and 100!",
    'volume_not_implemented': "🔧 Volume control requires additional setup. Use your system volume for now.",
    'error_playing': "❌ Error playing song: {error}",
    'missing_argument': "❌ Missing required argument! Use `{prefix}help` for command usage.",
    'command_error': "❌ An error occurred: {error}",
    
    # Info messages
    'specify_volume': "🔊 Please specify a volume level (0-100)",
    'bot_connected': "✅ {bot_name} has connected to Discord!",
    'music_folder_info': "📁 Music folder: {folder_path}",
    'songs_found': "🎵 Found {count} MP3 files",
    'intents_disabled': "ℹ️ Message Content Intent is disabled. Bot will respond to mentions only.",
    'intents_info': "💡 To use {prefix} commands, enable Message Content Intent in Discord Developer Portal.",
}

# =============================================================================
# HELP COMMAND CONFIGURATION
# =============================================================================

HELP_CONFIG = {
    'title': "🎵 MuskaBot Help",
    'color': 0x0099ff,  # Blue color for embeds
    'description_template': """
**Music Bot Commands:**
`{prefix}{join}` - Join your voice channel
`{prefix}{leave}` - Leave the voice channel
`{prefix}{play} <song_name>` - Play a specific song
`{prefix}{pause}` - Pause current playback
`{prefix}{resume}` - Resume paused playback
`{prefix}{stop}` - Stop current playback
`{prefix}{list}` - List all available songs
`{prefix}{random}` - Play a random song
`{prefix}{current}` - Show currently playing song
`{prefix}{help}` - Show this help message

**Usage Tips:**
• Place your MP3 files in the `music` folder
• You can use partial song names (e.g., `{prefix}{play} bohemian` for "Bohemian Rhapsody.mp3")
• Make sure you're in a voice channel before using music commands
    """,
    'intents_note': "\n\n**Note:** Message Content Intent is disabled. Use `@{bot_name} command` format."
}

# =============================================================================
# SONG LIST CONFIGURATION
# =============================================================================

LIST_CONFIG = {
    'title': "Available Songs",
    'color': 0x00ff00,  # Green color
    'bullet_point': "♪",  # Character before each song name
    'max_length': 1900,   # Max characters per message (Discord limit is 2000)
}

# =============================================================================
# STARTUP MESSAGES
# =============================================================================

STARTUP_MESSAGES = {
    'music_folder_created': "📁 Created {folder} folder. Place your MP3 files here!",
    'bot_starting': "🚀 Starting MuskaBot...",
    'token_instructions': [
        "🔑 Please set your Discord bot token!",
        "You can either:",
        "1. Create a .env file and set DISCORD_BOT_TOKEN=your_token",
        "2. Set the environment variable DISCORD_BOT_TOKEN", 
        "3. Edit config.py and replace YOUR_BOT_TOKEN_HERE",
        "",
        "To get a bot token:",
        "1. Go to https://discord.com/developers/applications",
        "2. Create a new application and bot",
        "3. Copy the bot token"
    ]
}
