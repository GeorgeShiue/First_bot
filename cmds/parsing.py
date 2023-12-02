import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension #從core資料夾中的classes檔案import Cog_Extension
import requests
from bs4 import BeautifulSoup

class Parsing(Cog_Extension):
    @commands.command()
    async def apex_map_routine(self, ctx, num: int = 24):
        await ctx.send('Parsing data...')
        res = requests.get('https://apexlegendsstatus.com/current-map/battle_royale/pubs')
        soup = BeautifulSoup(res.text, 'html.parser')

        content_map_name = []
        maps = soup.find_all("h3", style = "padding: 10px; margin: 0; font-weight: bolder;")
        for map in maps:
            content_map_name.append(str(map.text))

        content_map_time = []
        times = soup.find_all("p", style = "color: white; font-size: 1.7rem; margin-bottom: 0; padding-bottom: 10px;")
        for time in times:
            #await ctx.send(str(time.txt)) #時間無法直接輸出，需先丟進串列後再輸出(原因不明)
            content_map_time.append(str(time.text))

        count_day = [] #調時差
        for i in range(len(content_map_time)):
            temp1 = int(content_map_time[i][5:7]) + 8
            if temp1 >= 24:
                temp1 = temp1 - 24
            if temp1 == 0:
                count_day.append(i)

            temp2 = int(content_map_time[i][14:16]) + 8
            if temp2 >= 24:
                temp2 = temp2 - 24

            content_map_time[i] = list(content_map_time[i])
            del content_map_time[i][5:7]
            del content_map_time[i][12:14]
            content_map_time[i].insert(5, str(temp1))
            content_map_time[i].insert(13, str(temp2))
            content_map_time[i] = "".join(content_map_time[i])
            #print(content_map_time[i])
        for index in count_day:
            content_map_time.insert(index, '(The Next Day)')

        for i in range(num):
            if content_map_time[i] == '(The Next Day)':
                print(content_map_time[i])
                await ctx.send(content_map_time[i])
            else:
                print(content_map_name[i] + ":" + content_map_time[i])
                await ctx.send(content_map_name[i] + ": " + content_map_time[i])
        await ctx.send("Parsing over")
        print("Parsing over")

    @commands.command()
    async def baseball(self, ctx, title: str):
        url = "https://www.ptt.cc/bbs/Baseball/search?q=" + title
        resp = requests.get(url)
        # 將結果存在 Source.html 裡面
        with open("Source.html", "w", encoding="UTF-8") as f:
            f.write(resp.text)

        with open("Source.html", "r", encoding="UTF-8") as f:
            bs = BeautifulSoup(f.read(), features="html.parser")

        count = 0
        today = str(datetime.date.today())
        dates = bs.find_all("div", attrs={"class": "date"})
        for date in dates:
            date = date.text.replace('/','-')
            if date[1:5] == today[6:10]:
                count += 1

        temp = count
        titles = []
        links = bs.find_all("div", attrs={"class": "title"})
        for link in links:
            titles.append(link.text.strip())
            temp -= 1
            if temp == 0:
                break

        temp = count
        links_ = []
        for link in bs.find_all('a'):
            if title in link.text:
                links_.append("https://www.ptt.cc" + link.get('href'))
                temp -= 1
                if temp == 0:
                    break

        def SplitTitle(title: str, num: str):
            if "本文已被刪除" in title:
                return
            if "[" not in title:
                return
            if "]" not in title:
                return

            b = title.index("]")
            title = title[b + 1 :].strip()
            return num + ". " + title

        count = 0
        for t in titles:
            count += 1
            #print(SplitTitle(t, str(count)))

            count = 0
        for i in range(len(titles)):
            count += 1
            print(SplitTitle(titles[i], str(count)) + " " + links_[i])
            await ctx.send(SplitTitle(titles[i], str(count)) + " " + links_[i])

async def setup(bot):
    await bot.add_cog(Parsing(bot)) #新增Parsing底下的Cog