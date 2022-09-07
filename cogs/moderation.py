import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog is online")

    @commands.command(
        aliases=["clear"],
        example="a!purge 20",
        description="Purges messages in a channel including the one you sent"
    )
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, *, amount_of_messages):
        if int(amount_of_messages) >= 200:
            embed = discord.Embed(title=f"An error has occured",
                                  description=f"You have specified a number of messages to "
                                              f"delete higher than the amount allowed (200 or less is allowed)")
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1 + int(amount_of_messages))

    @commands.command(
        aliases=["permakick"],
        example="a!ban <@bob the builder>",
        description="Bans a specified player"
    )
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        author_id = ctx.author.id
        embed = discord.Embed(title=f"{member} has been banned",
                              description=f"The User has been banned by <@{author_id}>")
        await ctx.send(embed=embed)

    '''@commands.command(
        description="WIP"
    )
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
            await ctx.message.delete()'''

    @commands.command(
        example="a!kick <@bob the builder>",
        description="Kicks a member"
    )
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        author_id = ctx.author
        embed = discord.Embed(title=f"{member} has been kicked", description=f"The User has been kicked by {author_id}")
        await ctx.send(embed=embed)

    @commands.command(
        example="a!unban <@bob the builder>",
        description="bans and unbans someone"
    )
    @has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await asyncio.sleep(0.1)
        await ctx.guild.unban(member)
        await ctx.send(f"{member.mention} has been banned and unbanned")

    @commands.command(
        aliases=["changenick", "nickname"],
        example="a!nick <@bob the builder> bob"
    )
    async def nick(self, ctx, member: discord.Member, *, nickname):
        await member.edit(nick=nickname)
        await ctx.message.delete()

    @commands.command(
        aliases=["pm", "dm"],
        example="a!message <member>",
        description="messages a member"
    )
    @has_permissions(administrator=True)
    async def message(self, ctx, member: discord.Member, *, message):
        server = ctx.message.guild.name
        embed = discord.Embed(title=f"New Message from {server}", description=message)
        await member.send(embed=embed)
        await ctx.message.delete()

    @commands.command(
        example="a!embed \"bob\" he builds buildings",
        description="Sends a title and description using embed, useful for todo lists, etc"
    )
    @has_permissions(manage_messages=True)
    async def embed(self, ctx, title, *, description):
        embed = discord.Embed(title=title, description=description)
        await ctx.message.delete()
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Moderation(bot))
