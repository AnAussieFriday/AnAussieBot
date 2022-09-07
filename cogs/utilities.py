import discord
from urllib.parse import quote_plus
from discord.ext import commands
from typing import Optional


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utilities cog is online")

    @commands.command(aliases=["add", "join"], example="a!invite", description="invites someone to server")
    async def invite(self, ctx):
        url = discord.utils.oauth_url(str(self.bot.user.id))
        url2 = discord.utils.oauth_url("573680244213678081")
        embed = discord.Embed(title="Invites for bot",
                              description=f"**Here is the bot's invite:** [Invite]({url})"
                                          f"\n**Here is the "
                                          f"discord server for the bot**: https://discord.gg/fbZXXeUY4a\n**H"
                                          f"ere is the amazing G"
                                          f"oldbot's invite**: [Invite]({url2})")
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["av", "userpic", "useravatar", "userpicture"],
        example="a!avatar <@Bob The Builder>",
        description="A Command that retrieves the images of a user's avatar"
    )
    async def avatar(self, ctx: commands.Context, user: Optional[discord.User]):
        if user is None:
            user = ctx.author
        name = user.name
        avatar = user.avatar.url
        embed = discord.Embed(title=f"{name}'s avatar")
        embed.set_image(url=f"{avatar}")
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


async def setup(bot):
    await bot.add_cog(Utilities(bot))
