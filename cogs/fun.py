import random
import discord
from discord.ext import commands
import aiohttp

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun cog is online")


    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot: 
           pass
        else:
           msg = ctx.content.lower().split()
           if 'neat' in msg:
               await ctx.reply("Neat is a mod by Vaskii")


    @commands.command(
        aliases=["destroy"],
        example="a!kill bob the builder",
        description="Sends random kill message of someone",
        name="a!kill"
    )
    async def kill(self, ctx, *, victim):
        death_messages = [f'{victim} was stabbed',
                          f'{victim} was shot',
                          f'{victim} died of bad instrument playing aka violin 2 section',
                          f'{victim} was killed by overshipping',
                          f'{victim} got sick and **perished**',
                          f'{victim} was pinged to death',
                          f'{victim} did too much membean',
                          f'{victim} got too concerned and died <:concernes:965114973800001586>']
        await ctx.send(f'{random.choice(death_messages)}')

    @commands.command(
        example="a!reddit memes",
        description="WIP"
    )
    async def reddit(self, ctx, reddit):
        embed = discord.Embed(title=f"From r/{reddit}", description="Sorted by in hot **(COMMAND IS WIP)**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://www.reddit.com/r/{reddit}/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)


    @commands.command()
    async def dayswithoutbitches(self, ctx):
        await ctx.send('Days gone without the word "bitches" being said: **' + str(0) + '**')

    @commands.command()
    async def walterwhite(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/955314816166277152/966701687207248003/walter.mp4')

    @commands.command(aliases=['wisdom'],name="8ball",description="Ask the 8ball a question, it will deliver an answer most of the time i think")
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt',
                     'Yes definitely.',
                     'You may rely on it.',
                     'as I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes',
                     'Reply hazy, try again.',
                     'Ask again later',
                     'Better not tell you now.',
                     'Cannot predict now',
                     'Concentrate and ask again',
                     'My reply is no',
                     'Don\'t count on it',
                     'My sources say no.',
                     'Outlook not so good',
                     'Very doubtful']
        if question.endswith("?"):
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        else:
            embed = discord.Embed(title=f"Not a Question",
                                  description=f"How do I answer something thats not a question?")
            await ctx.send(embed=embed)

    @commands.command(
        aliases=["relationship","relation_ship"],
        example="a!ship urmom urdad",
        description="Ships 2 people together"
    )
    async def ship(self, ctx, ship_1, *, ship_2):
        loved = random.randint(0, 100)
        await ctx.send(f"{ship_1} x {ship_2}. They love each other {str(loved)}%")

    @commands.command(
        aliases=["stabone"],
        example="a!starborne",
        description="Chicken Avian Yes funny dont ask ok but bob"
    )
    async def starborne(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/924090195752661002/997936093632667768/starborne.gif")

    @commands.command(
        aliases=["dice"],
        example="a!roll 20",
        description="Picks a random number you give it"
    )
    async def roll(self, ctx, roll_number: int = 6):
        if roll_number == 6:
            number_dice_answer_2 = random.randint(1, roll_number)
            await ctx.send("<:game_die:975615039732068393> Out of 6 numbers, the dice landed on **" + str(
                number_dice_answer_2) + "**")
        else:
            number_dice_answer_2 = random.randint(1, roll_number)
            await ctx.send(f"Out of **{str(roll_number)}**, You got **{number_dice_answer_2}**")


    @commands.command(
        aliases=["burn","insult"],
        example="a!roast Bob the Builder",
        description="Roasts someone of your input"
    )
    async def roast(self, ctx, *, victim):
        death_messages = [f'**{victim}** is what happens when someone drinks while pregnant',
                          f'I wish I can go back to the moment I met **{victim}**, and walk past them',
                          f'You are the sun in my life... Why isn\'t **{victim}** 93 million miles away',
                          f'There is someone out there everyone needs, for **{victim}**, it is a therapist',
                          f'I would smack **{victim}**, but I am against animal abuse',
                          f'Cannot wait to live without **{victim}**!',
                          f'Whoever told **{victim}** to be themself, is a dumb person',
                          f'If **{victim}** was drowning, I would give them a hi-five',
                          f"If I throw a stick, will **{victim}** leave to get it? \nYes",
                          f"**{victim}** was given the ability of... being dumb. *At birth*",
                          f"Whatever **{victim}** is immune to, makes me sad",
                          f"**{victim}** have a nice day. ***Somewhere else***",
                          f"The therapy dog is scared of **{victim}**",
                          f"Every Therapist has a dream... To never meet **{victim}**",
                          f"The only thing bothering me in this room is the space between **{victim}**'s ears"
                          ]
        await ctx.send(f'{random.choice(death_messages)}')


    @commands.command(
        aliases=["choice","pick"],
        example="a!choose bob builder build buildings",
        description="Chooses one of many input you give it"
    )
    async def choose(self, ctx, *choices: str):
        await ctx.send(f"Out of {', '.join(choices)}, I choose **{random.choice(choices)}**")

    @commands.command(
        aliases=["memes"],
        example="a!meme",
        description="Sends a meme from one of 3 meme subreddits"
    )
    async def meme(self, ctx):
        reddits = ['https://www.reddit.com/r/dankmemes/new.json?sort=hot',
                           'https://www.reddit.com/r/memes/new.json?sort=hot',
                           'https://www.reddit.com/r/me_irl/new.json?sort=hot']
        async with aiohttp.ClientSession() as cs:
            async with cs.get(random.choice(reddits)) as r:
                res = await r.json()
                meme = res["data"]["children"][random.randint(0, 25)]
                image = meme["data"]["url"]
                title = meme["data"]["title"]
                reddit = meme["data"]["subreddit"]
                embed = discord.Embed(title=title, description=f"From r/{reddit}")
                embed.set_image(url=image)
                await ctx.send(embed=embed)

    @commands.command(
        aliases=["cats"],
        example="a!cat",
        description="Sends an image of a cat"
    )
    async def cat(self, ctx):
        cat_moment = [
            "https://tenor.com/view/kitty-review-cute-kitty-funny-cat-cat-review-gif-21188467",
            "https://tenor.com/view/kitty-review-gif-21953250",
            "https://tenor.com/view/seals-emporium-kitty-review-gif-21748019",
            "https://tenor.com/view/kitty-review-kitty-cat-cat-review-cat-long-legs-gif-21264306",
            "https://tenor.com/view/kitty-review-kitty-cat-cat-review-fat-cat-gif-21197159",
            "https://tenor.com/view/kitty-review-cat-review-gif-21140352",
            "https://tenor.com/view/kitty-review-gif-22546039",
            "https://tenor.com/view/kitty-review-bag-cat-gif-21320259",
            "https://cdn.discordapp.com/attachments/914233052828409857/994692085955440794/gilbertwest.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994692118721347654/gilbert.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691983761223751/cat-flying.gif",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691921572266034/88qcjk8syvr81.mp4",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691794656841940/6b8wup.gif",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691730714677349/Untitled.mp4",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691615077711954/trim.5B61D550-62CB-4AC8-B067-41358BBC6A0C.mov",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691545674559538/happiness.mp4",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691456256192696/5fa5f69ceee792b4.mp4",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691421934190713/cockey_cola.mp4",
            "https://cdn.discordapp.com/attachments/914233052828409857/994691202047803532/floppa-1.mp4",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690655093801080/Screenshot_155.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690653642567841/Screenshot_603.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690653424468028/Screenshot_605.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690653168619611/Screenshot_609.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690261760344144/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690261429006476/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690261206716526/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690260703395952/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690260309135380/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690259981959319/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690110257893486/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690109804916857/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690109217705994/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690108907335690/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690108211077130/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690107598704801/unknown.png",
            "https://cdn.discordapp.com/attachments/914233052828409857/994690107275751464/unknown.png"
        ]
        #ty to merpous for sending me this images and videos
        await ctx.send(f'{random.choice(cat_moment)}')


    #code doesn't work, disabled it for now

    #@commands.Cog.listener()
    #async def on_message_delete(self, message):
    #    self.bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel, message.created_at)

    #@commands.Cog.listener()
    #async def on_message_edit(self, before, after):
    #    self.bot.edited_messages = (before.content, after.content, after.author, after.author.avatar.url)

    #new = None

    #@commands.command()
    #async def snipe(self, ctx):
    #    content, user, channel, time = self.bot.sniped_messages[ctx.guild.id]
    #    edit_content_before, edit_content_after, edit_author, edit_author_avatar = self.bot.edited_messages
    #    new = None
    #    if new == None:
    #        embed = discord.Embed(description=f"**Before:** {edit_content_before}\n**After:** {edit_content_after}")
    #        embed.set_author(name=f"{edit_author}", icon_url=edit_author_avatar)
    #        await ctx.send(embed=embed)
    #        embed = discord.Embed(description=content, timestamp=time)
    #        embed.set_author(name=f"{user}", icon_url=user.avatar.url)
    #        embed.set_footer(text=f"Deleted in: #{channel}")
    #        await ctx.send(embed=embed)
    #    else:
    #        await ctx.send("Secret message kek")

async def setup(bot):
    await bot.add_cog(Fun(bot))
