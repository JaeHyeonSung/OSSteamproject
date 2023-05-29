# 락현 추가 수정#

import discord
import asyncio
import datetime
import requests, json
from discord.ext import commands
import time
from deep_translator import GoogleTranslator

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')


@bot.event
async def on_message(message):
    
    content = message.content

    if message.author.bot:
        return None
    if message.content.endswith("지도"):        #대구대지도를 끝말 '지도'로 불러옴
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/대구대지도.JPG")
        await message.channel.send(file=file)
        await message.channel.send("대구대 지도입니다.\n 다음과 같은 명령어를 입력시 해당 대학의 지도가 출력됩니다.\n 간호대학, 경영대학, 공과대학, 과학생명융합대학, 법행정대학, 사범대학, 사회과학대학, 인문대학, 재활과학대학, 정보통신대학, 조형예술대학")

    if message.content.startswith("과학생명융합") or "과생융" in content:   # 과학생명융합대학 지도를 불러옴 키워드 "과학생명융합대학 , 과생융"  (대학 지도는 대구대 홈페이지 2023 대학 기준 지도)
        file1 = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/과학생명융합대학1호관.png")
        file2 = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/과학생명융합대학2호관.png")
        file3 = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/과학생명융합대학3호관.png")
        file4 = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/과학생명융합대학5호관.png")
        file5 = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/과학생명융합대학6호관.png")
        await message.channel.send(file=file1)
        await message.channel.send(file=file2)
        await message.channel.send(file=file3)
        await message.channel.send(file=file4)
        await message.channel.send(file=file5)
        await message.channel.send("과학생명융합대학 지도입니다. \n '과생융' 키워드를 이용해 간편하게 입력하세요. ")
        
    if message.content.startswith("간호대"):
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/간호대학.png")
        await message.channel.send(file=file)
        await message.channel.send("간호대학 지도입니다.")

    if message.content.startswith("법행대"):
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/법행정대학.png")
        await message.channel.send(file=file)
        await message.channel.send("법행대학 지도입니다.")

    if message.content.startswith("경영대"):
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/경영대학.png")
        await message.channel.send(file=file)
        await message.channel.send("경영대학 지도입니다.")

    if message.content.startswith("공과대") or "공대" in content:
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/공과대학.png")
        await message.channel.send(file=file)
        await message.channel.send("공과대학 지도입니다. \n '공대' 키워드를 이용해서 간편하게 입력하세요.")


    if message.content.startswith("사범대") or "사대" in content:
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/공과대학.png")
        await message.channel.send(file=file)
        await message.channel.send("사범대학 지도입니다. \n '사대' 키워드를 이용해서 간편하게 입력하세요.")

    if message.content.startswith("사회과학대") or "사과대" in content:
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/사회과학대학.png")
        await message.channel.send(file=file)
        await message.channel.send("사회과학대학 지도입니다. \n '사과대' 키워드를 이용해서 간편하게 입력하세요.")

    if message.content.startswith("인문대"):
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/인문과학대학.png")
        await message.channel.send(file=file)
        await message.channel.send("인문대학 지도입니다.")

    if message.content.startswith("재활과학대학") or "재과대" in content:
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/재활과학대학.png")
        await message.channel.send(file=file)
        await message.channel.send("재활과학 지도입니다. \n '재과대' 키워드를 통해 간편하게 입력하세요")
        

    if message.content.startswith("정보통신대학") or "정통대" in content:
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/사회과학대학.png")
        await message.channel.send(file=file)
        await message.channel.send("정보통신대학 지도입니다. \n '정통대' 키워드를 통해 간편하게 입력하세요")
   
    if message.content.endswith("조형예술대학") or "조예대" in content:
        file = discord.File("/Users/krh/Downloads/OSSteamproject-master/image/조형예술대학.png")
        await message.channel.send(file=file)
        await message.channel.send("조형예술대학 지도입니다. \n '조예대' 키워드를 통해 간편하게 입력하세요")



bot.run('MTExMjMwMTgzMDk1Mzc3MTAwOA.GXG7Pb.Cv_tMCeTWEV483sfGXKhvnyjL19GcsSxLiz9w4')