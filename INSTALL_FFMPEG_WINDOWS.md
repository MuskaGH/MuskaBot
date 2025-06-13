# Install FFmpeg on Windows - Step by Step

## Method 1: Download and Install (Recommended)

### Step 1: Download FFmpeg
1. Go to https://ffmpeg.org/download.html
2. Click on "Windows" 
3. Click on "Windows builds by BtbN" (recommended)
4. Download the latest "ffmpeg-master-latest-win64-gpl.zip"

### Step 2: Extract FFmpeg
1. Create a folder: `C:\ffmpeg`
2. Extract the downloaded zip file to `C:\ffmpeg`
3. You should now have: `C:\ffmpeg\bin\ffmpeg.exe`

### Step 3: Add to System PATH
1. Press `Windows + R`, type `sysdm.cpl`, press Enter
2. Click "Environment Variables" button
3. In "System Variables" section, find and select "Path"
4. Click "Edit"
5. Click "New"
6. Add: `C:\ffmpeg\bin`
7. Click "OK" on all windows

### Step 4: Verify Installation
1. **IMPORTANT**: Close and reopen your command prompt/terminal
2. Run: `ffmpeg -version`
3. You should see FFmpeg version information

## Method 2: Using Chocolatey (If you have it)

If you have Chocolatey package manager installed:
```cmd
choco install ffmpeg
```

## Method 3: Using Winget (Windows 10/11)

```cmd
winget install ffmpeg
```

## After Installation

1. **Restart your command prompt/terminal**
2. Test FFmpeg: `ffmpeg -version`
3. Run your Discord bot: `python music_bot.py`
4. Try playing a song: `!play Matouš Takouš`

## Troubleshooting

**Still getting "ffmpeg not found"?**
- Make sure you restarted your command prompt after adding to PATH
- Verify the path `C:\ffmpeg\bin\ffmpeg.exe` exists
- Try running `where ffmpeg` to see if it's found

**Permission issues?**
- Run command prompt as Administrator when adding to PATH
- Make sure the ffmpeg.exe file isn't blocked by antivirus

## Quick Test

After installation, you can test if FFmpeg works with your MP3:
```cmd
ffmpeg -i "music/Matouš Takouš.mp3" -f null -
```

This should show information about your MP3 file without errors.
