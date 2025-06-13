# MuskaBot Troubleshooting Guide

## Common Issues and Solutions

### 1. PrivilegedIntentsRequired Error

**Error Message:**
```
discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal.
```

**Solution:**
This error occurs when the bot tries to use privileged intents that aren't enabled. You have two options:

#### Option A: Disable Privileged Intents (Recommended for basic functionality)
1. Open `config.py`
2. Set `INTENTS_MESSAGE_CONTENT = False`
3. The bot will work with slash commands and mentions

#### Option B: Enable Privileged Intents in Discord Developer Portal
1. Go to https://discord.com/developers/applications
2. Select your bot application
3. Go to the "Bot" section
4. Scroll down to "Privileged Gateway Intents"
5. Enable "Message Content Intent" if you want the bot to respond to `!` commands
6. Save changes
7. In `config.py`, set `INTENTS_MESSAGE_CONTENT = True`

### 2. Bot Token Issues

**Error Message:**
```
Please set your Discord bot token!
```

**Solution:**
You need to provide your bot token. Choose one method:

#### Method 1: Environment Variable (Most Secure)
1. Create a `.env` file in the MuskaBot folder
2. Add: `DISCORD_BOT_TOKEN=your_actual_token_here`
3. Never share this file

#### Method 2: Direct Configuration
1. Open `config.py`
2. Replace `YOUR_BOT_TOKEN_HERE` with your actual token
3. **Warning:** Don't commit this to version control

### 3. FFmpeg Not Found

**Error Message:**
```
FFmpeg was not found
```

**Solution:**
Install FFmpeg for your operating system:

#### Windows:
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your system PATH
4. Restart command prompt

#### macOS:
```bash
brew install ffmpeg
```

#### Linux:
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4. Bot Not Responding to Commands

**Possible Causes:**
- Bot is offline
- Missing permissions
- Wrong command prefix
- Privileged intents not configured

**Solutions:**
1. Check bot is online in Discord server
2. Ensure bot has these permissions:
   - Send Messages
   - Connect (voice)
   - Speak (voice)
   - Use Voice Activity
3. Try mentioning the bot: `@YourBot help_music`
4. Check privileged intents configuration

### 5. Audio Not Playing

**Possible Causes:**
- Not in a voice channel
- Missing voice permissions
- Corrupted MP3 files
- FFmpeg issues

**Solutions:**
1. Join a voice channel before using `!play`
2. Check bot has Connect and Speak permissions
3. Test with different MP3 files
4. Verify FFmpeg installation

### 6. No MP3 Files Found

**Error Message:**
```
No MP3 files found in the music folder!
```

**Solution:**
1. Ensure MP3 files are in the `music` folder
2. Check file extensions are `.mp3`
3. Avoid special characters in filenames
4. Restart bot after adding files

### 7. Permission Denied Errors

**Solution:**
1. Run command prompt as Administrator (Windows)
2. Use `sudo` for installation commands (Linux/macOS)
3. Check file/folder permissions

### 8. Import Errors

**Error Message:**
```
ModuleNotFoundError: No module named 'discord'
```

**Solution:**
Install required packages:
```bash
pip install -r requirements.txt
```

If still having issues:
```bash
pip install discord.py[voice] PyNaCl python-dotenv
```

## Getting Help

If you're still having issues:

1. Check the console output for specific error messages
2. Verify all setup steps in `setup_guide.md`
3. Ensure your Python version is 3.8 or higher
4. Try running the bot in a fresh terminal/command prompt

## Debug Mode

To get more detailed error information, you can enable debug logging by adding this to the top of `music_bot.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This will show more detailed information about what the bot is doing and any errors it encounters.
