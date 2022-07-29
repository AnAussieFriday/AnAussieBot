import random
import discord
from discord.ext import commands
import requests
from urllib.parse import quote_plus
from discord.ext.commands import is_owner
import aiohttp
import typing


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utilities cog is online")

    @commands.command(aliases=["add"])
    async def invite(self, ctx):
        await ctx.send("**Here is the bot's invite:** https://discord.com/api/oauth2/authorize?client_id=973663164568846386&permissions=8&scope=bot\n**Here is the discord server for the bot**: https://discord.gg/fbZXXeUY4a")

    @commands.command(aliases=["av", "userpic", "useravatar", "userpicture"])
    async def avatar(self, ctx: commands.Context, user: discord.User):
        name = user.name
        picture = user.avatar.url
        embed = discord.Embed(title=f"{name}'s avatar")
        embed.set_image(url=picture)
        await ctx.send(embed=embed)

    @commands.command()
    #i hard coded because i am too lazy to make a proper one
    async def help(self, ctx, *, category=None):
        if category == "8ball":
            await ctx.send(
                "**The 8ball command:** \nAsk the 8-ball a question, it will answer it\n**Example:** c!8ball <question>?\n**Aliases:** `wisdom`")
        elif category == "ban":
            await ctx.send(
                "**The Ban command:** \n**Description: **Ban a Person with it, only admins can use it\n**Example:** c!ban <member> <reason>\n**Aliases:** `none`")
        elif category == "dayswithoutbitches":
            await ctx.send(
                "**The bitches command:** \n**Description:** Counts the days without the word \"bitches\" being said\n**Example:** c!dayswithoutbitches\n**Aliases:** `none`")
        elif category == "dice":
            await ctx.send(
                "**The Dice command:** \n**Description:** Rolls a dice\n**Example:** c!dice\n**Aliases:** `die`")
        elif category == "help":
            await ctx.send(
                "**The help command:** \n**Description:** A command that portrays command description/commands\n**Example:** c!help <command>\n**Aliases:** `none`")
        elif category == "invite":
            await ctx.send(
                "**The Invite command:** \n**Description:** Displays the Invite link\n**Example:** c!invite\n**Aliases:** `add`")
        elif category == "kick":
            await ctx.send(
                "**The Kick command:** \n**Description:** Kicks the person specified, only people who are admins can do this\n**Example:** c!kick <member> <reason>\n**Aliases:** `none`")
        elif category == "kill":
            await ctx.send(
                "**The Kill command:** \n**Description:** Pretends to kill the person specified\n**Example:** c!kill <victim>\n**Aliases:** `none`")
        elif category == "purge":
            await ctx.send(
                "**The Purge command:** \n**Description:** Deletes massive chunks of messages\n**Example:** c!purge <amount_of_messages>\n**Aliases:** `none`")
        elif category == "roll":
            await ctx.send(
                "**The Roll command:** \n**Description:** Rolls the number specified\n**Example:** c!roll <number>\n**Aliases:** `none`")
        elif category == "say":
            await ctx.send(
                "**The say command:** \n**Description:** Sends a message using the bot (only owner can do this)\n**Example:** c!say <message>\n**Aliases:** `none`")
        elif category == "ship":
            await ctx.send(
                "**The ship command:** \n**Description:** Ships 2 people together\n**Example:** c!ship <first person> <second person>\n**Aliases:** `none`")
        elif category == "unban":
            await ctx.send(
                "**The Unban command:** \n**Description:** Unbans Banned People\n**Example:** c!unban <member>\n**Aliases:** `none`")
        elif category == "walterwhite":
            await ctx.send(
                "**The Rap command:** \n**Description:** Sends the chad walter white rap song\n**Example:** c!walterwhite\n**Aliases:** `none`")
        elif category == "nick":
            await ctx.send(
                "**The Nickname Change command:** \n**Description:** Changes the Nickname of specified user, people who can manage nicknames can only do this\n**Example:** c!nick <member> <nickname>\n**Aliases:** `nickname, changenick`")
        elif category == "message":
            await ctx.send(
                "**The Messaging command:** \n**Description:** DMs the specified user, users with admin perms can use it\n**Example:** c!dm <member> <message>\n**Aliases:** `dm, pm`")
        elif category == "embed":
            await ctx.send(
                "**The Embed command:** \n**Description:** Embed a title and description into a blocky message, users with manages message perms can use it\n**Use:** c!embed <title> <description> [colour]\n**Examples:** c!embed \"Title\" \"this is a description\"\n**Aliases:** `none`")
        elif category == "yesbutno":
            await ctx.send(
                "**The Yes but really No command:** \n**Description:** Yes but no image moment\n**Use:** c!yesbutno \n**Examples:** c!yesbutno\n**Aliases:** `none`")
        elif category == "avatar":
            await ctx.send(
                "**The Avatar command:** \n**Description:** Grabs the image of specified image\n**Use:** c!avatar <user>\n**Aliases:** `av`,`useravatar`,`userpic`,`userpicture`")
        elif category == "google" or category == "search":
            await ctx.send(
                "**The Search command:** \n**Description:** Searches then links you to search\n**Use:** c!search ur mom\n**Aliases:** `google`")
        elif category == "modrinth":
            await ctx.send(
                "**The Modrinth command:** \n**Description:** Searches a mod on modrinth\n**Use:** a!search modrinth Unwieldy\n**Aliases:** `none`")
        elif category == "modrinth":
            await ctx.send(
                "**The Bug/Suggestion command:** \n**Description:** Sends Suggestions or Bug Reports to AnAussieFriday#3675 \n**Use:** a!`suggest`/`bug` This Command Has a bug\n**Aliases for suggest:** `suggestion`\n**Aliases for bug:** `bugreport`,`bug_report`")
        elif category == "mcskin":
            await ctx.send(
                "**The Minecraft command:** \n**Description:** Pulls up the image of a player's model from NC \n**Use:** a!minecraft <type> <user>\n**Aliases `none`\n**Types:** `avatars` (sends the face), `head` (sends render of the head), `body` (sends render of head and body), `skin` (sends the skin file of the player)")
        else:
            embed = discord.Embed(title=f"**Help List**",
                                  description=f"\n__Fun Commands:__\n`8ball`\n`dayswithoutbitches`\n`insult`\n`kill`\n`roll`\n`walterwhite`\n__Moderating Commands:__\n`kick`\n`softban`\n`ban`\n`unban`\n`nick`\n`message`\n__Utility Commands:__\n`avatar`\n`search`\n`modrinth`\n`bug`\n`suggest`\n`mcskin`")
            await ctx.send(embed=embed)

    @commands.command()
    async def modrinth(self, ctx, *, mod):
        limit = {
            "limit": 1
        }
        if mod == "KFA":
            r = requests.get(f'https://api.modrinth.com/api/v1/mod?query=Kentucky Fried Axolotls', params=limit)
            for mod in r.json()[f'hits']:
                embed = discord.Embed(title=f'{mod["title"]}', description=f'{mod["description"]}',
                                      url=f'{mod["page_url"]}', colour=discord.Colour.random())
                embed.set_thumbnail(url=f'{mod["icon_url"]}')
                embed.add_field(name="Author", inline=True, value=f'{mod["author"]}: {mod["author_url"]}')
                embed.add_field(name="Downloads", value=f'{mod["downloads"]}', inline=True)
                embed.add_field(name="Follows", value=f'{mod["follows"]}', inline=True)
                embed.add_field(name="Versions", value=f'{", ".join(mod["versions"])}', inline=False)
                embed.add_field(name="Categories", value=f'{", ".join(mod["categories"])}', inline=False)
                await ctx.send(embed=embed)
        else:
            r = requests.get(f'https://api.modrinth.com/api/v1/mod?query={mod}', params=limit)
            for mod in r.json()[f'hits']:
                embed = discord.Embed(title=f'{mod["title"]}', description=f'{mod["description"]}',
                                      url=f'{mod["page_url"]}', colour=discord.Colour.random())
                embed.set_thumbnail(url=f'{mod["icon_url"]}')
                embed.add_field(name="Author", inline=True, value=f'{mod["author"]}: {mod["author_url"]}')
                embed.add_field(name="Downloads", value=f'{mod["downloads"]}', inline=True)
                embed.add_field(name="Follows", value=f'{mod["follows"]}', inline=True)
                embed.add_field(name="Versions", value=f'{", ".join(mod["versions"])}', inline=False)
                embed.add_field(name="Categories", value=f'{", ".join(mod["categories"])}', inline=False)
                await ctx.send(embed=embed)

    @commands.command(description='Sends "Pong!" and my latency.')
    async def ping(self, ctx):
        await ctx.send(f'Ping: {self.bot.latency * 1000:.0f}ms')

    class Search(discord.ui.View):
        def __init__(self, search: str):
            super().__init__()
            search_name = search
            search = quote_plus(search)
            url = f'https://www.google.com/search?q={search}'
            self.add_item(discord.ui.Button(label=search_name, url=url))

    @commands.command(aliases=["search"])
    async def google(self, ctx, *, search: str):
        await ctx.send(f"Search Result for: `{search}`", view=self.Search(search))

    @commands.command()
    async def mcskin(self, ctx, type, username=None):
        mc_website = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        name = mc_website.json()["id"]
        list = ["skin","body","head","avatar","avatars"]
        if type == "avatar" or type == "avatars":
            await ctx.send(f'https://crafatar.com/avatars/{name}.png')
        elif type == "head":
            await ctx.send(f'https://crafatar.com/renders/head/{name}.png')
        if type == "body":
            await ctx.send(f'https://crafatar.com/renders/body/{name}.png')
        if type == "skin":
            await ctx.send(f'https://crafatar.com/skins/{name}.png')
        elif type != list and username == None:
            mc_website = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{type}")
            name = mc_website.json()["id"]
            await ctx.send(f'https://crafatar.com/renders/body/{name}.png')
        else:
            pass

    @commands.command()
    @is_owner()
    async def say(self, ctx, channel: typing.Optional[discord.TextChannel], *, msg):
        if channel == None:
            channel = ctx.channel
        await ctx.message.delete()
        await channel.send(msg)


async def setup(bot):
    await bot.add_cog(Utilities(bot))