import disnake
from disnake.ext import commands

from dotenv import load_dotenv; load_dotenv()
import os

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.getenv('TOKEN'))