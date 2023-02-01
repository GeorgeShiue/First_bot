import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extension #從core資料夾中的classes檔案import Cog_Extension

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile) #開啟json設定檔並讀取裡面的所有資料

class React(Cog_Extension):
    @commands.command() #指令
    async def random_pic(self,ctx): 
        random_pic_path = random.choice(jdata['pic']) #設定變數來隨機儲存其中一個目標檔案路徑
        pic = discord.File(random_pic_path) #設定變數來儲存目標檔案
        #pic = discord.File(jdata["pic"]) #設定變數並放入目標檔案路徑來儲存目標檔案
        await ctx.send(file = pic) #傳送檔案

    @commands.command() #指令
    async def random_web_pic(self,ctx): 
        random_pic_url = random.choice(jdata['pic_url']) #設定變數隨機儲存其中一個目標圖片的網址
        await ctx.send(random_pic_url) #傳送網址

async def setup(bot):
    await bot.add_cog(React(bot)) #新增React底下的Cog