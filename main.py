import discord
from discord.ext import commands
import os
import asyncio
import sys
import aussiehelp


class Bot(commands.Bot):
    def __init__(self, *, intents: discord.Intents):

        prefix_list = ["a!", "b!", "c!"]

        super().__init__(command_prefix=prefix_list, intents=intents,help_command=aussiehelp.AnAussieHelpCommand())

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
        await bot.start(BEST_TOKEN_IN_THE_WORLD)
        #finally fixed the problem here


asyncio.run(main())


