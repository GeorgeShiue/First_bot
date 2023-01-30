import discord
from discord.ext import commands

bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '[') #intents告訴discord bot要用哪些功能，command_prefix為每次打指令前需要先用的符號

@bot.event #事件
async def on_ready():
    print(">> Bot is online <<")

bot.run("MTA2ODU1ODg5MzgzNzQ2MzU3Mg.GUu1Kb.KqLVZBYas5TAgGj1ywzysfzN1vT6Iit3-FQmdc") #discord bot token