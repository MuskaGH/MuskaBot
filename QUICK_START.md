# MuskaBot - Quick Start Guide

## 🎵 Discord Music Bot for MP3 Files

Your Discord music bot is ready! This bot can play MP3 files from your local computer directly in Discord voice channels.

## ⚡ Quick Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install FFmpeg
- **Windows**: Download from https://ffmpeg.org, extract, add to PATH
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### 3. Get Discord Bot Token
1. Go to https://discord.com/developers/applications
2. Create new application → Bot section → Copy token
3. **Keep this token secret!**

### 4. Set Your Token
**Option A (Recommended):**
Create `.env` file:
```
DISCORD_BOT_TOKEN=your_actual_token_here
```

**Option B:**
Edit `config.py` and replace `YOUR_BOT_TOKEN_HERE`

### 5. Add Music & Run
1. Put MP3 files in the `music` folder
2. Run: `python music_bot.py` or double-click `run_bot.bat`

## 🎮 Commands

- `!join` - Bot joins your voice channel
- `!play <song>` - Play MP3 (supports partial names)
- `!pause` / `!resume` - Control playback
- `!stop` - Stop music
- `!list` - Show all songs
- `!random` - Play random song
- `!help_music` - Show help

## 🔧 Troubleshooting

**Bot not responding?**
- Check `troubleshooting.md` for detailed solutions
- Most common: Enable "Message Content Intent" in Discord Developer Portal

**No audio?**
- Make sure you're in a voice channel
- Check FFmpeg installation
- Verify bot has voice permissions

## 📁 Project Structure

```
MuskaBot/
├── music_bot.py          # Main bot file
├── config.py             # Configuration
├── requirements.txt      # Dependencies
├── music/               # Put MP3 files here
├── setup_guide.md       # Detailed setup
├── troubleshooting.md   # Problem solutions
└── run_bot.bat         # Windows launcher
```

## ✅ Features

✅ Play local MP3 files  
✅ Partial song name matching  
✅ Basic playback controls  
✅ Random song selection  
✅ Automatic music folder creation  
✅ Secure token management  
✅ Error handling & help  

## 🚀 Ready to Rock!

Your Discord music bot is fully functional and ready to play your MP3 collection!

Need help? Check `troubleshooting.md` or `setup_guide.md` for detailed instructions.
