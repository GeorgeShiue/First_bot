import discord
from discord.ext import commands

class Cog_Extension(commands.Cog): #設定Cog_Extension使後續程式可以繼承commands.Cog和下列程式碼
    def __init__(self, bot):
        self.bot = bot #設定類別裡的bot就是主檔案裡的bot