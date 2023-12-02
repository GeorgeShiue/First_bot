import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension #從core資料夾中的classes檔案import Cog_Extension
import asyncio

class Main(Cog_Extension): #繼承Cog_Extension
    @commands.command() #指令
    async def ping(self,ctx): #使用者使用ping指令時，ctx便會包含使用者名稱、id、所在伺服器、所在頻道等訊息
        await ctx.send(f'{round(self.bot.latency*1000, 2)}ms') #依據ctx所提供的訊息傳送ping值(bot.latency)

    @commands.command() #指令
    async def instruction(self, ctx):
        """
        機器人的指令說明
        """
        embed=discord.Embed(title="First_bot Instruction", description="以下指令的前綴符號為 '-'", color=0x09ece8, timestamp = datetime.datetime.now())
        embed.set_author(name="George", icon_url="https://i.imgur.com/n7Q2RIW.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/5TmegF4.png")
        embed.add_field(name="ping", value="顯示機器人的ping值", inline=True)
        embed.add_field(name="repeat message", value="機器人會取代使用者發出使用者輸入的message", inline=True)
        embed.add_field(name="delete num", value="num代表希望刪除的訊息量", inline=False)
        embed.add_field(name="delete2 time date", value="刪除date(年月日)中time(小時分鐘)以後的所有訊息 date默認為傳訊息當天", inline=True)
        embed.add_field(name="apex_map_routine num", value="num代表希望看到的即將到來的地圖數目 默認為未來24張地圖", inline=False)
        embed.add_field(name="baseball title", value="擷取今日ptt棒球版上以title為關鍵字的所有文章標題與連結", inline=False)
        embed.set_footer(text="0")
        await ctx.send(embed=embed)
        
    @commands.command() #指令
    async def repeat(self, ctx, *,msg): #原本訊息會以空格作為參數的分界，* 可將未知個參數全都看作是msg參數的一部分
        await ctx.message.delete() #刪除傳送的訊息
        await ctx.send(msg) #原本傳送的訊息改由機器人發送

    @commands.command() #指令
    async def delete(self, ctx, num: int): #註解num使參數自動轉換為int，num為傳入的訊息量
        await ctx.channel.purge(limit = num + 1) #在訊息來源的頻道裡刪除num個訊息
        if num == 1:
            msg = await ctx.send(f'{num} message is deleted')
        else:
            msg = await ctx.send(f'{num} messages are deleted')
        await asyncio.sleep(3)
        await msg.delete() #刪除變數裡所傳送的訊息

    @commands.command() #指令
    async def delete2(self, ctx, time: str, time2 = datetime.datetime.now().strftime("%Y%m%d")): #strftime可將時間戳記轉為字串
        final = time2 + time
        final_time = datetime.datetime.strptime(final, "%Y%m%d%H%M") #strptime可將字串轉為時間戳記
        await ctx.channel.purge(limit = 100, after = final_time) #刪除指定時間後的所有訊息，上限為一百則
        msg = await ctx.send(f'All messages after {final_time.strftime("%H:%M")} has been deleted')
        await asyncio.sleep(3)
        await msg.delete() #刪除變數裡所傳送的訊息
    
async def setup(bot):
    await bot.add_cog(Main(bot)) #新增Main底下的Cog