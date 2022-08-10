import discord
from discord.ext import commands
import requests
from urllib.parse import quote_plus
from googletrans import Translator
import googletrans
import math
import aussielang

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    translator = Translator()

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
        try:
            list = ["skin","body","head","avatar","avatars"]
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
            embed = discord.Embed(title=f"An Error Occured",description="That MC user does not exist")
            await ctx.send(embed=embed)

    @commands.command(
        aliases=["detect"],
        name="language",
        description="Detects the probability of the language the the sentence is in",
    )
    async def detect_lang(self, ctx, *, sentence):
        bob = self.translator.detect(sentence)
        bob2 = aussielang.languages_detect.get(bob.lang)
        bob3 = math.ceil(bob.confidence / 0.01) * 0.01
        await ctx.send(f"**Language:** {bob2}\n**Confidence:** {bob3}")

    @commands.command(
        name="translate",
        description="Translate a message"
    )
    async def translate_lang(self, ctx, sentence, *, language="english"):
        bob2 = aussielang.languages_translate.get(language)
        bob = self.translator.translate(sentence,dest=bob2)
        await ctx.send(f"**Translated from:** {sentence}\n**Translated to:** {bob.text}")

    @commands.command(
        description = "Translate from english to galactic or the other way around"
    )
    async def galactic(self, ctx, translate_mode,*, sentence: str):
        if translate_mode == "encode" or translate_mode == "encrypt":
            a = sentence.replace("a",'ᔑ')
            b = a.replace("b",'ʖ')
            c = b.replace("c","ᓵ")
            d = c.replace("d","↸")
            e = d.replace("e","ᒷ")
            f = e.replace("f","⋮")
            g = f.replace("g","⊣")
            h = g.replace("h","⍑")
            i = h.replace("i","╎")
            j = i.replace("j","⋮")
            k = j.replace("k","ꖌ")
            l = k.replace("l","ꖎ")
            m = l.replace("m","ᒲ")
            n = m.replace("n","リ")
            o = n.replace("o","𝙹")
            p = o.replace("p","!")
            q = p.replace("q","¡")
            r = q.replace("r","ᑑ")
            s = r.replace("s","∷")
            t = s.replace("t","ᓭ")
            u = t.replace("u","ℸ")
            v = u.replace("v","⍊")
            w = v.replace("w","∴")
            x = w.replace("x","̇/")
            y = x.replace("y","||")
            z = y.replace("z","⨅")
            z2 = z.replace(" "," ")
            await ctx.send(z2)
        elif translate_mode == "decode" or translate_mode == "decrypt":
            a = sentence.replace("ᔑ",'a')
            b = a.replace("ʖ",'b')
            c = b.replace("ᓵ","c")
            d = c.replace("↸","d")
            e = d.replace("ᒷ","e")
            f = e.replace("⋮","f")
            g = f.replace("⊣","g")
            h = g.replace("⍑","h")
            i = h.replace("╎","i")
            j = i.replace("⋮","j")
            k = j.replace("ꖌ","k")
            l = k.replace("ꖎ","l")
            m = l.replace("ᒲ","m")
            n = m.replace("リ","n")
            o = n.replace("𝙹","o")
            p = o.replace("!","p")
            q = p.replace("¡","q")
            r = q.replace("ᑑ","r")
            s = r.replace("∷","s")
            t = s.replace("ᓭ","t")
            u = t.replace("ℸ","u")
            v = u.replace("⍊","v")
            w = v.replace("∴","w")
            x = w.replace("̇/","x")
            y = x.replace("||","y")
            z = y.replace("⨅","z")
            z2 = z.replace(" "," ")
            await ctx.send(z2)
        else:
            await ctx.send("That is not a valid mode! Use either `decrypt`, `encrypt`, `decode`, or `encode`")

async def setup(bot):
    await bot.add_cog(Utilities(bot))
