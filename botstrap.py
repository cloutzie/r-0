import disnake
from disnake.ext import commands

from dotenv import dotenv_values; env=dotenv_values('.env')
import os
import asyncio

from src.func.parse import parser


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

    async def submit(ctx, image: disnake.Attachment):
        await ctx.response.defer()
        img = parser(await image.read())
        await ctx.followup.send(img)



bot.add_cog(Submissions(bot))
bot.run(env['TOKEN'])

