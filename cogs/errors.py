import discord
from discord.ext import commands
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
            embed = discord.Embed(title="An Error Occurred", description="You are missing a field")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(title="An Error Occurred", description="You are not owner")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="An Error Occurred", description="This command was not found")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="An Error Occurred", description="You are missing the required permissions")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title="An Error Occurred", description="Member not found")
            await ctx.send(embed=embed)
        elif isinstance(error, error.EINVAL):
            embed = discord.Embed(title="An Error Occurred", description="That is an invalid namespace")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="An Error Occurred", description="An unknown error occured")
            await ctx.send(embed=embed)
            t_back = traceback.format_exception(type(error), error, error.__traceback__)
            str_t_back = ""
            for line in t_back:
                str_t_back += line
            print(str_t_back)
            bob = await self.bot.fetch_channel(974868749914087485)
            await bob.send(f"<@729184686013939713>\n```py\n{str_t_back}```")


async def setup(bot):
    await bot.add_cog(Error(bot))
