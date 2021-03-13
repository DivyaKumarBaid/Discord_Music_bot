from keep_alive import keep_alive
import discord
import nacl
from discord import FFmpegPCMAudio
import youtube_dl
import os
import discord.utils
from discord.ext import commands, tasks
from itertools import cycle
from replit import db


client = commands.Bot(command_prefix='_')

song_played=[]

#before running install pip install pynacl
#for audio pip install ffmpeg


#infinite loop to play music 24X7 untill closed/stopped
@tasks.loop(seconds=10)
async def play_song(ctx, ch, channel, n):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
  for file in os.listdir("./"):
    if file.endswith(".mp3") and not ch.is_playing() and file not in song_played and not voice == None :
      ch.play(discord.FFmpegPCMAudio(file), after=lambda e: print('done', e))
      text = discord.Embed(
      title= "**Playing**",
      description = f" Playing {file} ",
      color= 53380,
      )
      text.set_author(name= "Discord_music_bot",
      icon_url= "https://upload.wikimedia.org/wikipedia/commons/2/2a/ITunes_12.2_logo.png")
      text.set_footer(text= ".help to know commands")
      await ctx.send(embed=text, delete_after=10.0)
      song_played.append(str(file))
  if len(song_played) == n:
    song_played.clear()


#when bot is ready
@client.event
async def on_ready():
  print("I am alive")

#play command to start an infinite loop

@client.command(help="Channel name is optional." , brief="This command plays song from the available ones.Providing channel name is optional without which it will play on General")
async def play(ctx, channel='General'):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
  #channel is the desired channel
  channel = discord.utils.get(ctx.guild.voice_channels, name=channel)
  if voice == None:
    await ctx.send(f"Joined **{channel}**")
  else:
    await ctx.voice_client.disconnect()
  ch = await channel.connect()
  await ctx.send(f"Playing on **{channel}** Channel")
  
  #get the number of songs and if none is present it will show up a message
  n=0
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      n=n+1
  if not n==0:
    play_song.start(ctx, ch, channel, n)
  else:
    text = discord.Embed(
    title= "**No Music**",
    description = "There is no music to play\nUse _add [url] to add a music",
    color= 53380,
    )
    text.set_author(name= "Discord_Music_bot",
    icon_url= "https://upload.wikimedia.org/wikipedia/commons/2/2a/ITunes_12.2_logo.png")
    text.set_footer(text= ".help to know commands")
    await ctx.send(embed=text)
    


#add music
@client.command(help='youtube link is required', brief='This adds a music to the playlist. The url must be of youtube')
async def add(ctx, urllink :str):

  text = discord.Embed(
  description = f"**Searching and loading the song.\nThis might take a few seconds depending the number and size of song**",
  color= 53380,
  )
  text.set_author(name= "Discord_music_bot" ,
  icon_url= "https://upload.wikimedia.org/wikipedia/commons/2/2a/ITunes_12.2_logo.png")
  text.set_footer(text= ".help to know commands")
  await ctx.send(embed=text)

  ydl_opts = {
        'format': 'bestaudio/best',

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
        ],

    }
  try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([urllink])
      text = discord.Embed(
      title= "**Song Added**",
      url= urllink,
      description = "Song is added to the Queue",
      color= 53380,
      )
      text.set_author(name= "Discord_music_bot",
      icon_url= "https://upload.wikimedia.org/wikipedia/commons/2/2a/ITunes_12.2_logo.png")
      text.set_footer(text= ".help to know commands")
      await ctx.send(embed=text)
  except :
    await ctx.send("Error")

  
#join vc
@client.command(help='This joins the bot to the asked Voice channel', brief ='This adds bot to the given channel and by default in General')
async def join(ctx, channel='General'):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
    channel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    if voice == None:
      text = discord.Embed(
      description = f"Joined **{channel}**",
      color= 53380,
      )
      text.set_author(name= "Discord_music_bot",
      icon_url= "https://upload.wikimedia.org/wikipedia/commons/2/2a/ITunes_12.2_logo.png")
      text.set_footer(text= ".help to know commands")
      await ctx.send(embed=text)
    else:
      await ctx.voice_client.disconnect()
    await channel.connect()

#leave vc and stop playing
@client.command(help='This stops the loop' ,brief='This stops the music playing and the bot leaves the voice channel')
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
    if voice == None:
      return
    await ctx.voice_client.disconnect()
    play_song.stop()
    await ctx.send("Have left the channel")

#lists song
@client.command(help="This shows the songs present in the directory" ,brief='This command lists all the songs available to play')
async def songs(ctx):
  s=0
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      text = discord.Embed(
      description = f"Song Name : {file[:-4]} ",
      color= 53380,
      )
      text.set_author(name= "Discord_music_bot",
      icon_url= "https://upload.wikimedia.org/wikipedia/commons/2/2a/ITunes_12.2_logo.png")
      text.set_footer(text= ".help to know commands")
      await ctx.send(embed=text)
      s=s+1
  if s==0:
    await ctx.send("There is no song")

#remove song
@client.command(help='The file name should be wiht mp3 extension' , brief='This command removes the specified file')
async def remove(ctx, *,name: str):
  song_there=os.path.isfile(name)
  try:
    if song_there:
      os.remove(name)
      await ctx.send(f'Removed Successfully')
    else:
      print(song_there)
  except :
    await ctx.send("Still Playing")

#removes every song
@client.command(help='The file name should be wiht mp3 extension' , brief='This command removes every0 available song')
async def clear_playlist(ctx):
  b=True
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      song_there=os.path.isfile(file)
      try:
        if song_there:
          os.remove(file)
        else:
          b=False
      except :
        await ctx.send("Still Playing") 
  if b:
    await ctx.send(f'Removed Successfully')


#clear
@client.command(help='This command clears text messages', brief='This command clears given number of messages and by default it clears last 5 text messages')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared last {amount} texts')
    
#checks for errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command Used. Type //help to know the commands'
                       )
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'Give proper values to the command an argument is missing')

keep_alive() #this keeps the bot alive

#runs bot
client.run(os.getenv('TOKEN'))
