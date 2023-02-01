import discord
from discord.ext import commands
from core.classes import Cog_Extension #從core資料夾中的classes檔案import Cog_Extension

class Main(Cog_Extension): #繼承Cog_Extension
    @commands.command() #指令
    async def ping(self,ctx): #使用者使用ping指令時，ctx便會包含使用者名稱、id、所在伺服器、所在頻道等訊息
        await ctx.send(f'{round(self.bot.latency*1000, 2)}ms') #依據ctx所提供的訊息傳送ping值(bot.latency)

async def setup(bot):
    await bot.add_cog(Main(bot)) #新增Main底下的Cog