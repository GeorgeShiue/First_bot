import discord
from discord.ext import commands
import json

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile) #開啟json設定檔並讀取裡面的所有資料

bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '-') #intents告訴discord bot要用哪些功能，command_prefix為每次打指令前需要先用的符號

@bot.event #事件
async def on_ready(): #機器人上線後會印出以下句子
    print(">> Bot is online <<")

@bot.event #事件
async def on_member_join(member): #member參數代表伺服器成員名稱
    channel = bot.get_channel(int(jdata["TEST_CHANNEL"])) #建立頻道變數並利用json設定檔存取裡面的目標頻道id(要將str強制轉換為int)
    await channel.send(f'sup {member}') #在目標頻道內發送訊息

@bot.event #事件
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["TEST_CHANNEL"]))
    await channel.send(f'adios {member}')

@bot.command() #指令
async def ping(ctx): #使用者使用ping指令時，ctx便會包含使用者名稱、id、所在伺服器、所在頻道等訊息
    await ctx.send(f'{round(bot.latency*1000, 2)}ms') #依據ctx所提供的訊息傳送ping值(bot.latency)

bot.run(jdata["TOKEN"]) #利用json設定檔存取裡面的discord bot token(類似字典)