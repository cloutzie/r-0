import disnake
from disnake.ext import commands

from dotenv import dotenv_values; env=dotenv_values('.env')
import os

import random
import asyncio

bot = commands.InteractionBot()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



bot.run(env['TOKEN'])

