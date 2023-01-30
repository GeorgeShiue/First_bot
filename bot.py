import discord
from discord.ext import commands

bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '[') #intents告訴discord bot要用哪些功能，command_prefix為每次打指令前需要先用的符號

@bot.event #事件
async def on_ready(): #機器人上線後會印出以下句子
    print(">> Bot is online <<")

@bot.event #事件
async def on_member_join(member): #member變數代表伺服器成員
    channel = bot.get_channel(1069466066759196783) #建立頻道變數並放入目標頻道id
    await channel.send(f'sup {member}') #在目標頻道內發送訊息

@bot.event #事件
async def on_member_remove(member):
    channel = bot.get_channel(1069466066759196783)
    await channel.send(f'adios {member}')

bot.run("MTA2ODU1ODg5MzgzNzQ2MzU3Mg.GUu1Kb.KqLVZBYas5TAgGj1ywzysfzN1vT6Iit3-FQmdc") #discord bot token