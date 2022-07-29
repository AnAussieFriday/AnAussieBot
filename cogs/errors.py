import random
import discord
from discord.ext import commands
import asyncio
import traceback

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Error cog is online")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="An Error Occured", description="You are missing a field")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(title="An Error Occured", description="You are not owner")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="An Error Occured", description="This command was not found")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="An Error Occured", description="You are missing the required permissions")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title="An Error Occured", description="Member not found")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="An Error Occured", description="An unknown error occured")
            await ctx.send(embed=embed)
            #thank you to Golder06 for letting me look into his code, (i found this)
            tback = traceback.format_exception(type(error), error, error.__traceback__)
            str_tback = ""
            for line in tback:
                str_tback += line
            print(str_tback)

async def setup(bot):
    await bot.add_cog(Error(bot))
