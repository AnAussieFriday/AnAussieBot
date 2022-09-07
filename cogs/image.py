import discord
from discord.ext import commands
import os
from PIL import ImageFilter, ImageEnhance, Image
import requests
from io import BytesIO
import validators
from typing import Optional
import robin_merlification as merlification
import imagedits


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Editing images sound fun")

    @commands.command(description='Gets the outline of the specified image link')
    async def outline(self, ctx, link):
        if validators.url(link):
            response = requests.get(link)
            img = Image.open(BytesIO(response.content))
            img = imagedits.GetOutline(img)
            img.save("outline.png")
            await ctx.send("Done!", file=discord.File(fp="outline.png"))
            os.remove("outline.png")
        else:
            embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
            await ctx.send(embed=embed)

    @commands.command(description='Not exactly efficient; Merlifies an Image, makes it like Merle\'s PFP',
                      aliases=["merlify"])
    async def merlification(self, ctx, mode: str, link: Optional[str]):
        member = ctx.author
        if mode == 'robin':
            if link is not None:
                if validators.url(link):
                    response = requests.get(link)
                    img = Image.open(BytesIO(response.content))
                    img.save("robin_image.png")
                    img = merlification.merlify("robin_image.png")
                    img.save("robin_merlification.png")
                    await ctx.send("Done!", file=discord.File(fp="robin_merlification.png"))
                    os.remove("robin_merlification.png")
                    os.remove("robin_image.png")
                else:
                    embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                    await ctx.send(embed=embed)
            else:
                if validators.url(member.display_avatar.url):
                    response = requests.get(member.display_avatar.url)
                    img = Image.open(BytesIO(response.content))
                    img.save("robin_image.png")
                    img = merlification.merlify("robin_image.png")
                    img.save("robin_merlification.png")
                    await ctx.send("Done!", file=discord.File(fp="robin_merlification.png"))
                    os.remove("robin_merlification.png")
                    os.remove("robin_image.png")
                else:
                    embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                    await ctx.send(embed=embed)
        elif mode == "thick":
            if link is not None:
                if validators.url(link):
                    response = requests.get(link)
                    img = Image.open(BytesIO(response.content))
                    img = imagedits.thick_merlify(img)
                    img.save("thick_merl.png")
                    await ctx.send("Done!", file=discord.File(fp="thick_merl.png"))
                    os.remove("thick_merl.png")
                else:
                    embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                    await ctx.send(embed=embed)
            else:
                if validators.url(member.display_avatar.url):
                    response = requests.get(member.display_avatar.url)
                    img = Image.open(BytesIO(response.content))
                    img = imagedits.thick_merlify(img)
                    img.save("thick_merl.png")
                    await ctx.send("Done!", file=discord.File(fp="thick_merl.png"))
                    os.remove("thick_merl.png")
                else:
                    embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                    await ctx.send(embed=embed)
        elif mode == "thin":
            if link is not None:
                if validators.url(link):
                    response = requests.get(link)
                    img = Image.open(BytesIO(response.content))
                    img = imagedits.thin_merlify(img)
                    img.save("thin_merl.png")
                    await ctx.send("Done!", file=discord.File(fp="thin_merl.png"))
                    os.remove("thin_merl.png")
                else:
                    embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                    await ctx.send(embed=embed)
            else:
                if validators.url(member.display_avatar.url):
                    response = requests.get(member.display_avatar.url)
                    img = Image.open(BytesIO(response.content))
                    img = imagedits.thin_merlify(img)
                    img.save("thin_merl.png")
                    await ctx.send("Done!", file=discord.File(fp="thin_merl.png"))
                    os.remove("thin_merl.png")
                else:
                    embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                    await ctx.send(embed=embed)
        elif mode == "old":
            response = requests.get(link)
            img = Image.open(BytesIO(response.content))
            enh = ImageEnhance.Color(img)
            color = enh.enhance(0.0)
            ench = ImageEnhance.Contrast(color)
            contrast = ench.enhance(3.0)
            img = contrast.convert("RGBA")
            datas = img.getdata()
            new_data = []
            for item in datas:
                if item[0] != 0 and item[1] != 0 and item[2] != 0 and item[0] != 255 and item[1] != 255 and item[2] != 255:
                    new_data.append((254, 166, 30, 255))
                else:
                    new_data.append(item)
            img.putdata(new_data)
            en = ImageEnhance.Sharpness(img)
            sharp = en.enhance(1.0)
            on = sharp.filter(ImageFilter.SMOOTH)
            on2 = on.filter(ImageFilter.SHARPEN)
            en = ImageEnhance.Sharpness(on2)
            sharp2 = en.enhance(1)
            sharp2.save("old.png")
            await ctx.send("Done!", file=discord.File(fp="old.png"))
            os.remove("old.png")
        else:
            embed = discord.Embed(title="An Error Occurred",
                                  description="Invalid mode, use either: `thick`, `tiny`, or `robin`")
            await ctx.send(embed=embed)

    @commands.command(description='Makes the image have a outline of Latte\'s pfp')
    async def lattify(self, ctx, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = Image.open(BytesIO(response.content))
                img = imagedits.lattify(img)
                img.save("lattified.png")
                await ctx.send("Done!", file=discord.File(fp="lattified.png"))
                os.remove("lattified.png")
            else:
                embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = Image.open(BytesIO(response.content))
                img = imagedits.lattify(img)
                img.save("lattified.png")
                await ctx.send("Done!", file=discord.File(fp="lattified.png"))
                os.remove("lattified.png")
            else:
                embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command(description='Makes the image have the outline of the unwieldy')
    async def unwieldify(self, ctx, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = Image.open(BytesIO(response.content))
                img = imagedits.unwieldify(img)
                img2 = Image.open("images/unwieldy.png")
                img2 = img2.resize((img.width, img.height))
                img2 = imagedits.GetOutline(img2)
                img = imagedits.Combine(img, img2)
                img.save("unwieldify.png")
                await ctx.send("Done!", file=discord.File(fp="unwieldify.png"))
                os.remove("unwieldify.png")
            else:
                embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = Image.open(BytesIO(response.content))
                img = imagedits.unwieldify(img)
                img2 = Image.open("images/unwieldy.png")
                img2 = img2.resize((img.width, img.height))
                img2 = imagedits.GetOutline(img2)
                img = imagedits.Combine(img, img2)
                img.save("unwieldify.png")
                await ctx.send("Done!", file=discord.File(fp="unwieldify.png"))
                os.remove("unwieldify.png")
            else:
                embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command()
    async def aussify(self, ctx, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = Image.open(BytesIO(response.content))
                img = imagedits.aussification(img)
                img.save("aussification.png")
                await ctx.send("Done!", file=discord.File(fp="aussification.png"))
                os.remove("aussification.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = Image.open(BytesIO(response.content))
                img = imagedits.aussification(img)
                img.save("aussification.png")
                await ctx.send("Done!", file=discord.File(fp="aussification.png"))
                os.remove("aussification.png")
            else:
                embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command()
    async def resize(self, ctx, width: int, height: int, link):
        if validators.url(link):
            response = requests.get(link)
            img = Image.open(BytesIO(response.content))
            img = img.resize((width, height))
            img.save("resize.png")
            await ctx.send("Done!", file=discord.File(fp="resize.png"))
            os.remove("resize.png")
        else:
            embed = discord.Embed(title="An Error Occurred", description="The Link was Invalid")
            await ctx.send(embed=embed)

    @commands.command()
    async def get_colour(self, ctx, link):
        if validators.url(link):
            response = requests.get(link)
            img = Image.open(BytesIO(response.content))
            img = img.convert('RGB')
            img = img.resize((1, 1))
            r, g, b = img.getpixel((-1, -1))
            embed = discord.Embed(title="Here are your values!", description=f"Red: {r}\nGreen: {g}\nBlue: {b}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
            await ctx.send(embed=embed)


    @commands.command()
    async def gigachad(self, ctx, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = BytesIO(response.content)
                img = imagedits.cutout(img, "images/ihatmyself.png")
                img.save("gigachad.png")
                await ctx.send("Done!", file=discord.File(fp="gigachad.png"))
                os.remove("gigachad.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = BytesIO(response.content)
                img = imagedits.cutout(img, "images/ihatmyself.png")
                img.save("gigachad.png")
                await ctx.send("Done!", file=discord.File(fp="gigachad.png"))
                os.remove("gigachad.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command()
    async def aaqilify(self, ctx, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = BytesIO(response.content)
                img = imagedits.cutout(img, "images/aaqil.png")
                img.save("aaqilify.png")
                await ctx.send("Done!", file=discord.File(fp="aaqilify.png"))
                os.remove("aaqilify.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = BytesIO(response.content)
                img = imagedits.cutout(img, "images/aaqil.png")
                img.save("aaqilify.png")
                await ctx.send("Done!", file=discord.File(fp="aaqilify.png"))
                os.remove("aaqilify.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command(
        aliases=["rat"]
    )
    async def rattify(self, ctx, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = BytesIO(response.content)
                rat = requests.get("https://cdn.discordapp.com/attachments/974868749914087485/1014271699694399518/resize.png")
                rat = BytesIO(rat.content)
                img = imagedits.cutout(img, rat)
                img.save("rat.png")
                await ctx.send("Done!", file=discord.File(fp="rat.png"))
                os.remove("rat.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = BytesIO(response.content)
                rat = requests.get("https://cdn.discordapp.com/attachments/974868749914087485/1014271699694399518/resize.png")
                rat = BytesIO(rat.content)
                img = imagedits.cutout(img, rat)
                img.save("rat.png")
                await ctx.send("Done!", file=discord.File(fp="rat.png"))
                os.remove("rat.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command(aliases=["mask"])
    async def mask_image(self, ctx, mask_link, link: Optional[str]):
        member = ctx.author
        if link is not None:
            if validators.url(link):
                response = requests.get(link)
                img = BytesIO(response.content)
                mask_response = requests.get(mask_link)
                mask_img = BytesIO(mask_response.content)
                img = imagedits.cutout(img, mask_img)
                img.save("mask.png")
                await ctx.send("Done!", file=discord.File(fp="mask.png"))
                os.remove("mask.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(member.display_avatar.url):
                response = requests.get(member.display_avatar.url)
                img = BytesIO(response.content)
                mask_response = requests.get(mask_link)
                mask_img = BytesIO(mask_response.content)
                img = imagedits.cutout(img, mask_img)
                img.save("mask.png")
                await ctx.send("Done!", file=discord.File(fp="mask.png"))
                os.remove("mask.png")
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)

    @commands.command(aliases=["theme", "betterdiscordtheme"])
    async def better_discord_theme(self, ctx, name, link: Optional[str]):
        if link is None:
            link = ctx.author.display_avatar.url
        css = f'''/**
        * @name {name} theme'''
        css3 = '''
        * @version Auto Update
        * @description A Theme Made from the AnAussieBot - Based on the Frosted Glass theme
        * @Source https://github.com/DiscordStyles/FrostedGlass
        * @website https://betterdiscord.app/theme/Frosted%20Glass
        */
        @import url("https://discordstyles.github.io/FrostedGlass/dist/FrostedGlass.css");
        :root {'''
        css2 = f'''
        --background-image: url('{link}');
        --background-image-blur: 0px;
        --background-image-size: contain;
        --background-image-position: center;
        --popout-modal-image: url('{link}');
        --popout-modal-blur: 0px;
        --popout-modal-size: cover;
        --popout-modal-position: center;
        --home-button-image: url('{link}');
        --home-button-size: cover;
        --home-button-position: center;
        --serverlist-brightness: 0.8;
        --left-brightness: 1;
        --middle-brightness: 0.75;
        --right-brightness: 1;
        --popout-modal-brightness: 0.5;
        --gradient-primary: 183,183,183;
        --gradient-secondary: 183,183,181;
        --gradient-direction: 360deg;
        --tint-colour: 255,255,255;
        --tint-brightness: 0;
        --window-padding: 0px;
        --window-roundness: 25px;
        --scrollbar-colour: #ffffff0d;
        --link-colour: #00b0f4;
        --show-gift-gif-buttons: block;
        --font: 'cairo';
        --update-notice-1: none;
        '''
        member = ctx.author
        if link is not None:
            if validators.url(member.display_avatar.url):
                file_name = f"{name}.theme.css"
                with open(f"{file_name}", 'w') as f:
                    f.write(f'{css}' + css3 + f'\n{css2}\n' + '}')
                await ctx.send("Done!", file=discord.File(fp=file_name))
                os.remove(file_name)
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)
        else:
            if validators.url(link):
                file_name = f"{name}.theme.css"
                with open(f"{file_name}", 'w') as f:
                    f.write(f'\n{css}' + css3 + f'\n{css2}\n' + '}')
                await ctx.send("Done!", file=discord.File(fp=file_name))
                os.remove(file_name)
            else:
                embed = discord.Embed(title="An Error Occured", description="The Link was Invalid")
                await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Images(bot))
