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
    """
    channel = bot.get_channel(1075381757194551377)
    await channel.send("輸入-instruction以獲得機器人的指令說明")
    await channel.send("輸入-help以查看所有可用的機器人指令")
    channel = bot.get_channel(int(jdata["TEST_CHANNEL"]))
    await channel.send("輸入-instruction以獲得機器人的指令說明")
    await channel.send("輸入-help以查看所有可用的機器人指令")
    channel = bot.get_channel(1075416612238270555)
    await channel.send("輸入-instruction以獲得機器人的指令說明")
    await channel.send("輸入-help以查看所有可用的機器人指令")
    """
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
