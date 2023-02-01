import discord
from discord.ext import commands
import json
import os
import asyncio

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

@bot.command()
async def wow(ctx):
    await ctx.send("wow")

@bot.command() #指令
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}') #讓bot可以load特定的extension
    await ctx.send(f'Loaded {extension} is done.')

@bot.command() #指令
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}') #讓bot可以unload特定的extension
    await ctx.send(f'Unloaded {extension} is done.')

@bot.command() #指令
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}') #讓bot可以reload特定的extension
    await ctx.send(f'Reloaded {extension} is done.')

#以下為新作法
async def main():
    for filename in os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(jdata["TOKEN"])

if __name__=="__main__":
    asyncio.run(main())

"""  
for file_name in os.listdir('./cmds'): #利用os.listdir遍歷目標資料夾底下的所有檔案
    print(file_name)
    if file_name.endswith('.py'): #若檔案名稱結尾為.py
        bot.load_extension(f'cmds.{file_name[:-3]}') #從cmds資料夾裡導入裡面的檔案，[:-3]可.py從檔名中省略  

if __name__ == '__main__':
    bot.run(jdata["TOKEN"]) #利用json設定檔存取裡面的discord bot token(類似字典)
"""