import random
import discord
from discord.ext import commands
import asyncio
import traceback
from discord.ext.commands import is_owner
import typing

class Hidden(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("The Hidden Cog is online... actually offline shhh")

    @commands.command()
    @is_owner()
    async def say(self, ctx, channel: typing.Optional[discord.TextChannel], *, msg):
        if channel == None:
            channel = ctx.channel
        await ctx.message.delete()
        await channel.send(msg)

    @commands.command(description="hi")
    @is_owner()
    async def cogs(self, ctx, action, cog):
        if action == "load":
            await self.bot.load_extension(f"cogs.{cog}")
        elif action == "unload":
            await self.bot.unload_extension(f"cogs.{cog}")
        else:
            await ctx.send("You have not specified load or unload")

    class funni_discord_button(discord.ui.View):
        def __init__(self):
            super().__init__()

        @discord.ui.button(label='Nice button', style=discord.ButtonStyle.green, emoji="👍")
        async def button_test(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("https://www.youtube.com/watch?v=dQw4w9WgXcQ", ephemeral=True)

    @commands.command()
    async def button(self, ctx, *, button_message):
        view = self.funni_discord_button()
        await ctx.send(f"{button_message}", view=view)


    @commands.command(aliases=["shoebill"],name=" ")
    async def shoebill_emoji(self, ctx, delete=None):
        if delete == "delete":
            await ctx.send("<:shoebill:977454370369204305>")
            await ctx.message.delete()
        else:
            await ctx.send("<:shoebill:977454370369204305>")


    @commands.command()
    async def windows8(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=fRTzdZcooro")

    @commands.command(
    )
    async def yesbutno(self, ctx):
        await ctx.send("https://tenor.com/view/well-yes-but-actually-no-well-yes-no-yes-yes-no-gif-13736934")

    @commands.command(
    )
    async def idk(self, ctx):
        embed = discord.Embed(title="idk", description="idk")
        await ctx.send(embed=embed)

    @commands.command(
    )
    async def test(self, ctx):
        pass


async def setup(bot):
    await bot.add_cog(Hidden(bot))