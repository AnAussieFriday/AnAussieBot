import discord
from discord.ext import commands
import requests
from urllib.parse import quote_plus


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utilities cog is online")

    @commands.command(aliases=["add","join"],example="a!invite",description="invites someone to server")
    async def invite(self, ctx):
        await ctx.send("**Here is the bot's invite:** https://discord.com/api/oauth2/authorize?client_id=973663164568846386&permissions=8&scope=bot\n**Here is the discord server for the bot**: https://discord.gg/fbZXXeUY4a")

    @commands.command(
        aliases=["av", "userpic", "useravatar", "userpicture"],
        example="a!avatar <@Bob The Builder>",
        description="A Command that retrieves the images of a user's avatar"
    )
    async def avatar(self, ctx: commands.Context, user: discord.User):
        name = user.name
        picture = user.avatar.url
        embed = discord.Embed(title=f"{name}'s avatar")
        embed.set_image(url=picture)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["mod"],
        example="a!modrinth KFA",
        description="Command that retrieves information about a mod on modrinth"
    )
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

    @commands.command(
        example="a!ping",
        description="Get my ping"
    )
    async def ping(self, ctx):
        await ctx.send(f'Ping: {self.bot.latency * 1000:.0f}ms')

    class Search(discord.ui.View):
        def __init__(self, search: str):
            super().__init__()
            search_name = search
            search = quote_plus(search)
            url = f'https://www.google.com/search?q={search}'
            self.add_item(discord.ui.Button(label=search_name, url=url))

    @commands.command(
        aliases=["search"],
        example="a!search bob the builder",
        description="Sends a button that links you somewhere, no reason why, its funny"
    )
    async def google(self, ctx, *, search: str):
        await ctx.send(f"Search Result for: `{search}`", view=self.Search(search))

    @commands.command(
        aliases=["minecraft"],
        example="a!mcskin body AustralianFriday",
        description="Sends a render of the player in the specified field (`head`, `skin`, `body`, `avatar`, `avatars`"
    )
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


async def setup(bot):
    await bot.add_cog(Utilities(bot))
