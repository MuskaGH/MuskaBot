# Discord Music Bot Setup Guide

## Prerequisites

1. **Python 3.8 or higher** - Make sure Python is installed on your system
2. **FFmpeg** - Required for audio processing
3. **Discord Bot Token** - You'll need to create a Discord application

## Step 1: Install FFmpeg

### Windows:
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the files to a folder (e.g., `C:\ffmpeg`)
3. Add the `bin` folder to your system PATH:
   - Open System Properties → Advanced → Environment Variables
   - Edit the PATH variable and add `C:\ffmpeg\bin`
   - Restart your command prompt

## Step 2: Install Python Dependencies

Open a terminal/command prompt in the MuskaBot directory and run:

```bash
pip install -r requirements.txt
```

## Step 3: Create a Discord Bot

1. Go to https://discord.com/developers/applications
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Click "Add Bot"
5. Under "Token", click "Copy" to copy your bot token
6. **Important**: Keep this token secret!

### Bot Permissions:
Make sure your bot has these permissions:
- Send Messages
- Connect (to voice channels)
- Speak (in voice channels)
- Use Voice Activity

## Step 4: Invite Bot to Your Server

1. In the Discord Developer Portal, go to "OAuth2" → "URL Generator"
2. Select "bot" in Scopes
3. Select the permissions mentioned above
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

## Step 5: Configure the Bot

1. Open `music_bot.py`
2. Find the line: `TOKEN = "YOUR_BOT_TOKEN_HERE"`
3. Replace `"YOUR_BOT_TOKEN_HERE"` with your actual bot token

## Step 6: Add Your Music

1. Create a `music` folder in the MuskaBot directory (it will be created automatically when you run the bot)
2. Place your MP3 files in this folder
3. The bot will automatically detect all `.mp3` files

## Step 7: Run the Bot

```bash
python music_bot.py
```

## Bot Commands

Once the bot is running, you can use these commands in Discord:

- `!join` - Bot joins your voice channel
- `!play <song_name>` - Play a specific song (you can use partial names)
- `!pause` - Pause current playback
- `!resume` - Resume paused playback
- `!stop` - Stop current playback
- `!leave` - Bot leaves the voice channel
- `!list` - Show all available songs
- `!random` - Play a random song
- `!current` - Show currently playing song
- `!help_music` - Show help message