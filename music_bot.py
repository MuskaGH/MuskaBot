import discord
from discord.ext import commands
import asyncio
import os
import random
from pathlib import Path
from config import BOT_TOKEN, COMMAND_PREFIX, MUSIC_FOLDER, INTENTS_MESSAGE_CONTENT, INTENTS_VOICE_STATES

# Bot configuration
intents = discord.Intents.default()
intents.message_content = INTENTS_MESSAGE_CONTENT
intents.voice_states = INTENTS_VOICE_STATES

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Music queue and current playing track
music_queue = []
current_track = None
voice_client = None

class MusicBot:
    def __init__(self):
        self.music_folder = MUSIC_FOLDER  # Folder where MP3 files are stored
        self.ensure_music_folder()
    
    def ensure_music_folder(self):
        """Create music folder if it doesn't exist"""
        if not os.path.exists(self.music_folder):
            os.makedirs(self.music_folder)
            print(f"Created {self.music_folder} folder. Place your MP3 files here!")
    
    def get_mp3_files(self):
        """Get all MP3 files from the music folder"""
        music_path = Path(self.music_folder)
        return list(music_path.glob("*.mp3"))
    
    def find_song(self, query):
        """Find a song by partial name match"""
        mp3_files = self.get_mp3_files()
        query_lower = query.lower()
        
        # Exact match first
        for file in mp3_files:
            if query_lower == file.stem.lower():
                return file
        
        # Partial match
        for file in mp3_files:
            if query_lower in file.stem.lower():
                return file
        
        return None

music_bot = MusicBot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Music folder: {os.path.abspath(music_bot.music_folder)}')
    mp3_files = music_bot.get_mp3_files()
    print(f'Found {len(mp3_files)} MP3 files')
    
    if not INTENTS_MESSAGE_CONTENT:
        print("Note: Message Content Intent is disabled.")
        print("Bot will respond to mentions and slash commands only.")
        print("To use ! commands, enable Message Content Intent in Discord Developer Portal.")

@bot.command(name='join')
async def join_voice_channel(ctx):
    """Join the voice channel of the user who sent the command"""
    global voice_client
    
    if ctx.author.voice is None:
        await ctx.send("You need to be in a voice channel to use this command!")
        return
    
    channel = ctx.author.voice.channel
    
    if voice_client is not None:
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()
    
    await ctx.send(f"Joined {channel.name}!")
    return voice_client

@bot.command(name='leave')
async def leave_voice_channel(ctx):
    """Leave the current voice channel"""
    global voice_client
    
    if voice_client is not None:
        await voice_client.disconnect()
        voice_client = None
        await ctx.send("Left the voice channel!")
    else:
        await ctx.send("I'm not in a voice channel!")

@bot.command(name='play')
async def play_music(ctx, *, song_name=None):
    """Play a specific MP3 file or resume playback"""
    global voice_client, current_track
    
    if voice_client is None:
        voice_client = await join_voice_channel(ctx)
        if voice_client is None:
            await ctx.send("Failed to join voice channel!")
            return
    
    if song_name is None:
        if voice_client and voice_client.is_paused():
            voice_client.resume()
            await ctx.send("Resumed playback!")
        else:
            await ctx.send("Please specify a song name or use `!list` to see available songs.")
        return
    
    # Find the song
    song_file = music_bot.find_song(song_name)
    if song_file is None:
        await ctx.send(f"Could not find song: {song_name}")
        return
    
    # Stop current playback if any
    if voice_client and voice_client.is_playing():
        voice_client.stop()
    
    # Play the song
    try:
        source = discord.FFmpegPCMAudio(str(song_file))
        if voice_client:
            voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
            current_track = song_file.stem
            await ctx.send(f"Now playing: **{current_track}**")
    except Exception as e:
        await ctx.send(f"Error playing song: {e}")

@bot.command(name='pause')
async def pause_music(ctx):
    """Pause the current playback"""
    global voice_client
    
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Paused playback!")
    else:
        await ctx.send("Nothing is currently playing!")

@bot.command(name='resume')
async def resume_music(ctx):
    """Resume paused playback"""
    global voice_client
    
    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Resumed playback!")
    else:
        await ctx.send("Nothing is paused!")

@bot.command(name='stop')
async def stop_music(ctx):
    """Stop the current playback"""
    global voice_client, current_track
    
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        current_track = None
        await ctx.send("Stopped playback!")
    else:
        await ctx.send("Nothing is currently playing!")

@bot.command(name='volume')
async def set_volume(ctx, volume: int = 50):
    """Set playback volume (0-100)"""
    if not 0 <= volume <= 100:
        await ctx.send("Volume must be between 0 and 100!")
        return
    
    # Note: Volume control requires a different audio source
    await ctx.send("Volume control requires additional setup. Use your system volume for now.")

@bot.command(name='list')
async def list_songs(ctx):
    """List all available MP3 files"""
    mp3_files = music_bot.get_mp3_files()
    
    if not mp3_files:
        await ctx.send("No MP3 files found in the music folder!")
        return
    
    song_list = "\n".join([f"• {file.stem}" for file in mp3_files])
    
    # Discord has a 2000 character limit for messages
    if len(song_list) > 1900:
        # Split into multiple messages if too long
        chunks = [song_list[i:i+1900] for i in range(0, len(song_list), 1900)]
        for i, chunk in enumerate(chunks):
            embed = discord.Embed(
                title=f"Available Songs (Part {i+1}/{len(chunks)})",
                description=chunk,
                color=0x00ff00
            )
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Available Songs",
            description=song_list,
            color=0x00ff00
        )
        await ctx.send(embed=embed)

@bot.command(name='random')
async def play_random(ctx):
    """Play a random MP3 file"""
    mp3_files = music_bot.get_mp3_files()
    
    if not mp3_files:
        await ctx.send("No MP3 files found!")
        return
    
    random_song = random.choice(mp3_files)
    await play_music(ctx, song_name=random_song.stem)

@bot.command(name='current')
async def current_song(ctx):
    """Show currently playing song"""
    global current_track, voice_client
    
    if current_track and voice_client and voice_client.is_playing():
        await ctx.send(f"Currently playing: **{current_track}**")
    else:
        await ctx.send("Nothing is currently playing!")

@bot.command(name='help_music')
async def help_music(ctx):
    """Show music bot commands"""
    bot_name = bot.user.name if bot.user else "BotName"
    prefix = COMMAND_PREFIX if INTENTS_MESSAGE_CONTENT else f"@{bot_name} "
    
    help_text = f"""
**Music Bot Commands:**
`{prefix}join` - Join your voice channel
`{prefix}leave` - Leave the voice channel
`{prefix}play <song_name>` - Play a specific song
`{prefix}pause` - Pause current playback
`{prefix}resume` - Resume paused playback
`{prefix}stop` - Stop current playback
`{prefix}list` - List all available songs
`{prefix}random` - Play a random song
`{prefix}current` - Show currently playing song
`{prefix}help_music` - Show this help message

**Usage Tips:**
• Place your MP3 files in the `music` folder
• You can use partial song names (e.g., `{prefix}play bohemian` for "Bohemian Rhapsody.mp3")
• Make sure you're in a voice channel before using music commands
    """
    
    if not INTENTS_MESSAGE_CONTENT:
        help_text += f"\n\n**Note:** Message Content Intent is disabled. Use `@{bot_name} command` format."
    
    embed = discord.Embed(
        title="🎵 Music Bot Help",
        description=help_text,
        color=0x0099ff
    )
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore unknown commands
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument! Use `!help_music` for command usage.")
    else:
        await ctx.send(f"An error occurred: {error}")

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Please set your Discord bot token!")
        print("You can either:")
        print("1. Create a .env file and set DISCORD_BOT_TOKEN=your_token")
        print("2. Set the environment variable DISCORD_BOT_TOKEN")
        print("3. Edit config.py and replace YOUR_BOT_TOKEN_HERE")
        print("\nTo get a bot token:")
        print("1. Go to https://discord.com/developers/applications")
        print("2. Create a new application and bot")
        print("3. Copy the bot token")
    else:
        print("Starting MuskaBot...")
        bot.run(BOT_TOKEN)
