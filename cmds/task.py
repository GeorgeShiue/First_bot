import datetime
import json
from discord.ext import commands, tasks
from core.classes import Cog_Extension #從core資料夾中的classes檔案import Cog_Extension

class Task(Cog_Extension):
    #以下和教學影片有多處不同
    def __init__(self, bot): #__init__會將某一類別裡的所有屬性格式化/初始化
        super().__init__(bot) #將原本希望繼承下來的類別裡的屬性再定義一次
        self.flag = 0 #用來判別是否已傳過訊息的變數

    @commands.command()
    async def set_time(self, ctx, time):
        self.flag = 0
        with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
            jdata = json.load(jfile) #開啟json設定檔並讀取裡面的所有資料
        jdata['time'] = time #存取使用者的指定時間
        with open('setting.json', mode = 'w', encoding = 'utf8') as jfile:
            json.dump(jdata, jfile, indent = 4) #開啟json設定檔並在jfile中寫入jdata，indent為縮排
        await ctx.send("Time is set")

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.flag = 0
        self.channel = self.bot.get_channel(ch) #獲取訊息中所指定的頻道代碼
        await ctx.send(f'Set Channel:{self.channel.mention}') #標記機器人即將發訊息的指定頻道

    @commands.command()
    async def start_msg(self, ctx):
        self.losers.start() #開始發送訊息
        await ctx.send('Message is waited to be sent')

    @tasks.loop(seconds = 3.0) #每隔3秒執行一次以下程式
    async def losers(self):
        now_time = datetime.datetime.now().strftime('%H%M') #存取現在時間，strftime裡可設定判定時間的單位
        with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
            jdata = json.load(jfile) #開啟json設定檔並讀取裡面的所有資料
        if now_time == jdata['time'] and self.flag == 0: #若現在時間與目標時間相符就執行以下程式
            await self.channel.send("Hey losers")
            self.flag = 1

    @losers.before_loop #在執行目標函式前先執行以下程式
    async def before_printer(self):
        await self.bot.wait_until_ready() #等到機器人準備好

    @commands.command()
    async def end_msg(self, ctx):
        self.losers.cancel() #終止發送訊息
        await ctx.send('Message is terminated')
        
    """
    def __init__(self, *args, **kwargs): #__init__會將某一類別裡的所有屬性格式化/初始化
        super().__init__(*args, **kwargs) #將原本希望繼承下來的類別裡的屬性再定義一次

    #async def setup_hook(self) -> None:
     #   self.bg_task = self.bot.loop.create_task(self.interval()) #設定背景作業

        async def interval(self):
            await self.bot.wait_until_ready() #等待機器人準備就緒
            self.channel = self.bot.get_channel('1069466066759196783')
            while not self.bot.is_closed(): #若機器人未被關閉便一直重複以下迴圈
                await self.channel.send("Hey losers")
                await asyncio.sleep(5) #以秒為單位作為重複程式的間隔

        self.bg_task = self.bot.loop.create_task(interval()) #設定背景作業
    """
async def setup(bot):
    await bot.add_cog(Task(bot))