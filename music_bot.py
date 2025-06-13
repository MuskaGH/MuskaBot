import discord
from discord.ext import commands
import asyncio
import os
import random
from pathlib import Path
from config import BOT_TOKEN, MUSIC_FOLDER, INTENTS_MESSAGE_CONTENT, INTENTS_VOICE_STATES
from commands_config import COMMAND_PREFIX, COMMANDS, MESSAGES, HELP_CONFIG, LIST_CONFIG, STARTUP_MESSAGES

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
            print(STARTUP_MESSAGES['music_folder_created'].format(folder=self.music_folder))
    
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
    print(MESSAGES['bot_connected'].format(bot_name=bot.user))
    print(MESSAGES['music_folder_info'].format(folder_path=os.path.abspath(music_bot.music_folder)))
    mp3_files = music_bot.get_mp3_files()
    print(MESSAGES['songs_found'].format(count=len(mp3_files)))
    
    if not INTENTS_MESSAGE_CONTENT:
        print(MESSAGES['intents_disabled'])
        print(MESSAGES['intents_info'].format(prefix=COMMAND_PREFIX))

@bot.command(name=COMMANDS['join'])
async def join_voice_channel(ctx):
    """Join the voice channel of the user who sent the command"""
    global voice_client
    
    if ctx.author.voice is None:
        await ctx.send(MESSAGES['not_in_voice'])
        return
    
    channel = ctx.author.voice.channel
    
    if voice_client is not None:
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()
    
    await ctx.send(MESSAGES['joined_channel'].format(channel_name=channel.name))
    return voice_client

@bot.command(name=COMMANDS['leave'])
async def leave_voice_channel(ctx):
    """Leave the current voice channel"""
    global voice_client
    
    if voice_client is not None:
        await voice_client.disconnect()
        voice_client = None
        await ctx.send(MESSAGES['left_channel'])
    else:
        await ctx.send(MESSAGES['not_in_channel'])

@bot.command(name=COMMANDS['play'])
async def play_music(ctx, *, song_name=None):
    """Play a specific MP3 file or resume playback"""
    global voice_client, current_track
    
    if voice_client is None:
        voice_client = await join_voice_channel(ctx)
        if voice_client is None:
            await ctx.send(MESSAGES['failed_to_join'])
            return
    
    if song_name is None:
        if voice_client and voice_client.is_paused():
            voice_client.resume()
            await ctx.send(MESSAGES['resumed'])
        else:
            prefix = COMMAND_PREFIX if INTENTS_MESSAGE_CONTENT else f"@{bot.user.name} " if bot.user else "@BotName "
            await ctx.send(MESSAGES['specify_song'].format(prefix=prefix))
        return
    
    # Find the song
    song_file = music_bot.find_song(song_name)
    if song_file is None:
        await ctx.send(MESSAGES['song_not_found'].format(song_name=song_name))
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
            await ctx.send(MESSAGES['now_playing'].format(track_name=current_track))
    except Exception as e:
        await ctx.send(MESSAGES['error_playing'].format(error=e))

@bot.command(name=COMMANDS['pause'])
async def pause_music(ctx):
    """Pause the current playback"""
    global voice_client
    
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send(MESSAGES['paused'])
    else:
        await ctx.send(MESSAGES['nothing_playing'])

@bot.command(name=COMMANDS['resume'])
async def resume_music(ctx):
    """Resume paused playback"""
    global voice_client
    
    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await ctx.send(MESSAGES['resumed'])
    else:
        await ctx.send(MESSAGES['nothing_paused'])

@bot.command(name=COMMANDS['stop'])
async def stop_music(ctx):
    """Stop the current playback"""
    global voice_client, current_track
    
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        current_track = None
        await ctx.send(MESSAGES['stopped'])
    else:
        await ctx.send(MESSAGES['nothing_playing'])

@bot.command(name=COMMANDS['volume'])
async def set_volume(ctx, volume: int = 50):
    """Set playback volume (0-100)"""
    if not 0 <= volume <= 100:
        await ctx.send(MESSAGES['volume_range'])
        return
    
    await ctx.send(MESSAGES['volume_not_implemented'])

@bot.command(name=COMMANDS['list'])
async def list_songs(ctx):
    """List all available MP3 files"""
    mp3_files = music_bot.get_mp3_files()
    
    if not mp3_files:
        await ctx.send(MESSAGES['no_songs_found'])
        return
    
    song_list = "\n".join([f"{LIST_CONFIG['bullet_point']} {file.stem}" for file in mp3_files])
    
    # Discord has a 2000 character limit for messages
    if len(song_list) > LIST_CONFIG['max_length']:
        # Split into multiple messages if too long
        chunks = [song_list[i:i+LIST_CONFIG['max_length']] for i in range(0, len(song_list), LIST_CONFIG['max_length'])]
        for i, chunk in enumerate(chunks):
            embed = discord.Embed(
                title=f"{LIST_CONFIG['title']} (Part {i+1}/{len(chunks)})",
                description=chunk,
                color=LIST_CONFIG['color']
            )
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=LIST_CONFIG['title'],
            description=song_list,
            color=LIST_CONFIG['color']
        )
        await ctx.send(embed=embed)

@bot.command(name=COMMANDS['random'])
async def play_random(ctx):
    """Play a random MP3 file"""
    mp3_files = music_bot.get_mp3_files()
    
    if not mp3_files:
        await ctx.send(MESSAGES['no_songs_found'])
        return
    
    random_song = random.choice(mp3_files)
    await play_music(ctx, song_name=random_song.stem)

@bot.command(name=COMMANDS['current'])
async def current_song(ctx):
    """Show currently playing song"""
    global current_track, voice_client
    
    if current_track and voice_client and voice_client.is_playing():
        await ctx.send(MESSAGES['currently_playing'].format(track_name=current_track))
    else:
        await ctx.send(MESSAGES['nothing_playing'])

@bot.command(name=COMMANDS['help'])
async def help_music(ctx):
    """Show music bot commands"""
    bot_name = bot.user.name if bot.user else "BotName"
    prefix = COMMAND_PREFIX if INTENTS_MESSAGE_CONTENT else f"@{bot_name} "
    
    help_text = HELP_CONFIG['description_template'].format(
        prefix=prefix,
        join=COMMANDS['join'],
        leave=COMMANDS['leave'],
        play=COMMANDS['play'],
        pause=COMMANDS['pause'],
        resume=COMMANDS['resume'],
        stop=COMMANDS['stop'],
        list=COMMANDS['list'],
        random=COMMANDS['random'],
        current=COMMANDS['current'],
        help=COMMANDS['help']
    )
    
    if not INTENTS_MESSAGE_CONTENT:
        help_text += HELP_CONFIG['intents_note'].format(bot_name=bot_name)
    
    embed = discord.Embed(
        title=HELP_CONFIG['title'],
        description=help_text,
        color=HELP_CONFIG['color']
    )
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore unknown commands
    elif isinstance(error, commands.MissingRequiredArgument):
        prefix = COMMAND_PREFIX if INTENTS_MESSAGE_CONTENT else f"@{bot.user.name} " if bot.user else "@BotName "
        await ctx.send(MESSAGES['missing_argument'].format(prefix=prefix))
    else:
        await ctx.send(MESSAGES['command_error'].format(error=error))

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        for line in STARTUP_MESSAGES['token_instructions']:
            print(line)
    else:
        print(STARTUP_MESSAGES['bot_starting'])
        bot.run(BOT_TOKEN)
