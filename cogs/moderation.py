import random
import discord
from discord.ext import commands
from discord.ext.commands import is_owner
from discord.ext.commands import CheckFailure, has_permissions
import asyncio
import json


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog is online")

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, *, amount_of_messages: int):
        if amount_of_messages == str:
            embed = discord.Embed(title=f"An error has occured",
                                 description=f"The value `amount_of_messages` cannot be a string or letter, must be a number below 200")
            await ctx.send(embed=embed)
        else:
            if amount_of_messages >= 200:
                #this has happened before do not question it
                embed = discord.Embed(title=f"An error has occured",
                                      description=f"You have specified a number of messages to delete higher than the amount allowed (200 or less is allowed)")
                await ctx.send(embed=embed)
            else:
                await ctx.channel.purge(limit=amount_of_messages)

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        id = ctx.author.id
        embed = discord.Embed(title=f"{member} has been banned", description=f"The User has been banned by <@{id}>")
        await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        pass
        #doesn't work, too lazy to debug
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                id = ctx.author.id
                embed = discord.Embed(title=f"{member} has been unbanned",
                                      description=f"The User has been unbanned by <@{id}>")
                await ctx.send(embed=embed)
                return
        else:
            await ctx.send(f"You do not have Administrator permissions")
            await ctx.message.delete()

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        id = ctx.authod
        embed = discord.Embed(title=f"{member} has been kicked", description=f"The User has been kicked by {id}")
        await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await asyncio.sleep(0.1)
        await ctx.guild.unban(member)
        await ctx.send(f"{member.mention} has been banned and unbanned")

    @commands.command(aliases=["nickname", "changenick"])
    async def nick(self, ctx, member: discord.Member, *, nickname):
        await member.edit(nick=nickname)
        await ctx.message.delete()

    @commands.command(aliases=["pm", "dm"])
    @has_permissions(administrator=True)
    async def message(self, ctx, member: discord.Member, *, message):
        server = ctx.message.guild.name
        embed = discord.Embed(title=f"New Message from {server}", description=message)
        await member.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @has_permissions(manage_messages=True)
    async def embed(self, ctx, title, *, description):
        embed = discord.Embed(title=title, description=description)
        await ctx.message.delete()
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Moderation(bot))