import random
import discord
from discord.ext import commands
import os
from discord.ext.commands import is_owner
import asyncio
from discord.ext.commands import CheckFailure, has_permissions
import aiohttp
import sys
from urllib.parse import quote_plus
import json
from discord import app_commands


class Bot(commands.Bot):
    def __init__(self, *, intents: discord.Intents):

        prefix_list = ["a!", "b!", "c!"]

        super().__init__(command_prefix=prefix_list, intents=intents, help_command=None)

    async def on_ready(self):
        await bot.change_presence(status=discord.Status.online,
                                     activity=discord.Activity(type=discord.ActivityType.listening,
                                                               name="Walter White Rapping"))
        print('Logged in as a concerned {0.user}'.format(bot))


intents = discord.Intents.default()
intents.message_content = True

bot = Bot(intents=intents)


print(sys.version)


async def main():
    async with bot:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                #for some reason it only loads the first file and not the other :pensive:
                await bot.load_extension(f"cogs.utilities")
                await bot.load_extension(f"cogs.moderation")
                await bot.load_extension(f"cogs.fun")
            await bot.start(TOKEN)


@bot.command()
@is_owner()
async def cogs(ctx, action, cog):
    if action == "load":
        await bot.load_extension(f"cogs.{cog}")
    elif action == "unload":
        await bot.unload_extension(f"cogs.{cog}")
    else:
        await ctx.send("You have not specified load or unload")


asyncio.run(main())


