import json
from discord.ext import commands
from core.classes import Cog_Extension #從core資料夾中的classes檔案import Cog_Extension

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile) #開啟json設定檔並讀取裡面的所有資料

class Event(Cog_Extension):
    @commands.Cog.listener() #事件
    async def on_member_join(self, member): #member參數代表伺服器成員名稱
        channel = self.bot.get_channel(int(jdata["TEST_CHANNEL"])) #建立頻道變數並利用json設定檔存取裡面的目標頻道id(要將str強制轉換為int)
        await channel.send(f'sup {member}') #在目標頻道內發送訊息

    @commands.Cog.listener() #事件
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["TEST_CHANNEL"]))
        await channel.send(f'adios {member}')

    @commands.Cog.listener() #事件
    async def on_message(self, msg):
        simp = ['shylily', 'neuro', '蕾娜']
        if msg.content in simp: #若訊息內容含有特定字串
            await msg.channel.send('simp') #在訊息來源頻道裡發送新訊息
        elif msg.content.endswith('Joe'):
            await msg.channel.send('mama')
        elif 'sup' in msg.content and msg.author != self.bot.user: #防止洗頻
            await msg.channel.send('sup')

async def setup(bot):
    await bot.add_cog(Event(bot)) #新增Event底下的Cog