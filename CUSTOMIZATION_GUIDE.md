# MuskaBot Customization Guide

## 🎨 How to Customize Your Bot

Your Discord music bot is fully customizable! You can change command names, messages, colors, and the prefix without touching the main bot code.

## 📝 Configuration Files

### `config.py` - Basic Settings
- Bot token
- Music folder location
- Discord intents settings

### `commands_config.py` - Commands & Messages
- Command prefix and command names
- All bot messages and responses
- Help text and embed colors
- Startup messages

## 🔧 Common Customizations

### 1. Change Command Prefix

Edit `commands_config.py`:
```python
COMMAND_PREFIX = '?'  # Changes from ! to ?
```

Now commands become: `?play`, `?join`, `?list`, etc.

### 2. Change Command Names

Edit `commands_config.py`:
```python
COMMANDS = {
    'join': 'mjoin',       # !mjoin instead of !join
    'leave': 'mleave',     # !mleave instead of !leave
    'play': 'start',       # !start instead of !play
    'pause': 'break',      # !break instead of !pause
    'resume': 'continue',  # !continue instead of !resume
    'stop': 'end',         # !end instead of !stop
    'volume': 'vol',       # !vol instead of !volume
    'list': 'songs',       # !songs instead of !list
    'random': 'shuffle',   # !shuffle instead of !random
    'current': 'now',      # !now instead of !current
    'help': 'commands',    # !commands instead of !help_music
}
```

### 3. Customize Messages

Change any bot response in the `MESSAGES` dictionary:
```python
MESSAGES = {
    'joined_channel': "🎵 I'm here! Ready to rock in **{channel_name}**! 🎸",
    'now_playing': "🔥 Now jamming to: **{track_name}** 🔥",
    'paused': "⏸️ Taking a quick break!",
    'resumed': "▶️ Back to the music!",
    # ... customize any message
}
```

### 4. Change Colors and Appearance

Customize embed colors and list appearance:
```python
HELP_CONFIG = {
    'title': "🎵 My Custom Music Bot",
    'color': 0xff0000,  # Red color (hex)
}

LIST_CONFIG = {
    'title': "🎶 Your Playlist",
    'color': 0x00ff00,  # Green color
    'bullet_point': "🎵",  # Emoji before each song
}
```

## 🎨 Color Codes

Use these hex color codes for embeds:
- `0xff0000` - Red
- `0x00ff00` - Green  
- `0x0099ff` - Blue
- `0xffff00` - Yellow
- `0xff00ff` - Magenta
- `0x00ffff` - Cyan
- `0xffa500` - Orange
- `0x800080` - Purple
- `0xffc0cb` - Pink

## 📋 Message Variables

These variables can be used in messages:
- `{channel_name}` - Voice channel name
- `{track_name}` - Song name
- `{song_name}` - Requested song name
- `{error}` - Error message
- `{prefix}` - Command prefix
- `{bot_name}` - Bot's name
- `{folder_path}` - Music folder path
- `{count}` - Number of songs

## 🔄 How to Apply Changes

1. Edit `commands_config.py`
2. Save the file
3. Restart the bot: `python music_bot.py`
4. Changes take effect immediately!

## 🚨 Important Notes

- Don't change the keys in dictionaries (like `'join'`, `'play'`), only change the values
- Command names must be valid (no spaces, special characters)
- Color codes must be in hex format (0x followed by 6 digits)
- Always restart the bot after making changes

Your bot is now fully customizable! Have fun making it your own! 🎉
