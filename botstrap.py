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


class Submissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(
        name = 'submit',
        description = 'Submit runs for analysis'
    )

    async def submit(ctx, image: disnake.Attachment, image2: disnake.Attachment = None):
        await ctx.response.defer("Processing")
        
        await ctx.followup.send("Output")
        

bot.add_cog(Submissions(bot))
bot.run(env['TOKEN'])

