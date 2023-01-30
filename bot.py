import discord
from discord.ext import commands

bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '-') #intents告訴discord bot要用哪些功能，command_prefix為每次打指令前需要先用的符號

@bot.event #事件
async def on_ready(): #機器人上線後會印出以下句子
    print(">> Bot is online <<")

@bot.event #事件
async def on_member_join(member): #member參數代表伺服器成員名稱
    channel = bot.get_channel(1069466066759196783) #建立頻道變數並放入目標頻道id
    await channel.send(f'sup {member}') #在目標頻道內發送訊息

@bot.event #事件
async def on_member_remove(member):
    channel = bot.get_channel(1069466066759196783)
    await channel.send(f'adios {member}')

@bot.command() #指令
async def ping(ctx): #使用者使用ping指令時，ctx便會包含使用者名稱、id、所在伺服器、所在頻道等訊息
    await ctx.send(f'{round(bot.latency*1000, 2)}ms') #依據ctx所提供的訊息傳送ping值(bot.latency)

bot.run("MTA2ODU1ODg5MzgzNzQ2MzU3Mg.GUu1Kb.KqLVZBYas5TAgGj1ywzysfzN1vT6Iit3-FQmdc") #discord bot token