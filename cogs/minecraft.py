import discord
from discord.ext import commands
import requests


class Minecraft_Origins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Minecraft/Origins Cog is online")

    @commands.command(
        aliases=["minecraft"],
        example="a!mcskin body AustralianFriday",
        description="Sends a render of the player in the specified field (`head`, `skin`, `body`, `avatar`, `avatars`"
    )
    async def mcskin(self, ctx, type, username=None):
        mc_website = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        name = mc_website.json()["id"]
        try:
            list = ["skin", "body", "head", "avatar", "avatars"]
            if type == "avatar" or type == "avatars":
                await ctx.send(f'https://crafatar.com/avatars/{name}.png?overlay=true')
            elif type == "head":
                await ctx.send(f'https://crafatar.com/renders/head/{name}.png?overlay=true')
            if type == "body":
                await ctx.send(f'https://crafatar.com/renders/body/{name}.png?overlay=true')
            if type == "skin":
                await ctx.send(f'https://crafatar.com/skins/{name}.png?overlay=true')
            elif type != list and username == None:
                mc_website = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{type}?overlay=true")
                name = mc_website.json()["id"]
                await ctx.send(f'https://crafatar.com/renders/body/{name}.png?overlay=true')
            else:
                pass
        except:
            embed = discord.Embed(title=f"An Error Occured", description="That MC user does not exist")
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
                embed.add_field(name="Author", inline=True, value=f'[{mod["author"]}]({mod["author_url"]})')
                embed.add_field(name="Downloads", value=f'{mod["downloads"]}', inline=True)
                embed.add_field(name="Follows", value=f'{mod["follows"]}', inline=True)
                embed.add_field(name="Versions", value=f'{", ".join(mod["versions"])}', inline=False)
                embed.add_field(name="Categories", value=f'{", ".join(mod["categories"])}', inline=False)
                await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Minecraft_Origins(bot))
