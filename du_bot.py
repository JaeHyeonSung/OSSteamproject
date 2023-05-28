import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')


@bot.command()
async def hello(message):
    await message.channel.send('Hi!')

bot.run('Token')
