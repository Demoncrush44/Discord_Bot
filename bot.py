import discord
from discord.ext import commands
import os
import time
import responses
import requests
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv("TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!',intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @bot.command()
    async def cv(ctx, x,y):
        result = (float(x) *2) + float(y)
        await ctx.send(f"crit rate: {x} and crit damage: {y} = crit value of {result}")

    @bot.command()
    async def ct(ctx):
        URL = 'https://api.genshin.dev/materials/talent-book'
        r = requests.get(URL)
        res = r.json()
        freedom = res['freedom']['characters']
        resistance = res['resistance']['characters']
        ballad = res['ballad']['characters']
        prosperity = res['prosperity']['characters']
        gold = res['gold']['characters']
        diligence = res['diligence']['characters']
        transience = res['transience']['characters']
        light = res['light']['characters']
        elegance = res['elegance']['characters']

        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        now = time.localtime()
        weekday_index = now.tm_wday
        current_day= weekdays[weekday_index]

        freedom_characters =(' , '.join(str(a) for a in freedom))
        resistance_characters =(' , '.join(str(a) for a in resistance))
        ballad_characters =(' , '.join(str(a) for a in ballad))
        prosperity_characters=(' , '.join(str(a) for a in prosperity))
        gold_characters=(' , '.join(str(a) for a in gold))
        diligence_characters=(' , '.join(str(a) for a in diligence))
        transience_characters=(' , '.join(str(a) for a in transience))
        light_characters=(' , '.join(str(a) for a in light))
        elegance_characters=(' , '.join(str(a) for a in elegance))

        if current_day == 'Monday':
            await ctx.send(f"{freedom_characters} {prosperity_characters} {transience_characters} talent materials are available today!")
        elif current_day == 'Tuesday':
            await ctx.send(f"{resistance_characters} {diligence_characters} {elegance_characters} talent materials are available today!")
        elif current_day == 'Wednesday':
            await ctx.send(f"{ballad_characters} {gold_characters} {light_characters} talent materials are available today!")
        elif current_day == 'Thursday':
            await ctx.send(f"{freedom_characters} {prosperity_characters} {transience_characters} talent materials are available today!")
        elif current_day == 'Friday':
            await ctx.send(f"{resistance_characters} {diligence_characters} {elegance_characters} talent materials are available today!")
        elif current_day == 'Saturday':
            await ctx.send(f"{ballad_characters} {gold_characters} {light_characters} talent materials are available today!")
        elif current_day == 'Sunday':
            await ctx.send(f"{freedom_characters} {prosperity_characters} {transience_characters} {resistance_characters} {diligence_characters} {elegance_characters} {ballad_characters} {gold_characters} {light_characters} talent materials are available today!")
    

    @bot.command()
    async def talent(ctx):
        #temporary hardcoded statements
         weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
         now = time.localtime()
         weekday_index = now.tm_wday
         current_day= weekdays[weekday_index]
         if current_day == 'Monday':
            await ctx.send(f"Today is {current_day} and freedom, prosperity, transience, and admonition are available today")
         elif current_day == 'Tuesday':
            await ctx.send(f"Today is {current_day} and resistance, diligence, elegance, and ingenuity are available today")
         elif current_day == 'Wednesday':
            await ctx.send(f"Today is {current_day} and ballad, gold, light, and praxis are available today")
         elif current_day == 'Thursday':
            await ctx.send(f"Today is {current_day} and freedom, prosperity, transience, and admonition are available today")
         elif current_day == 'Friday':
            await ctx.send(f"Today is {current_day} and resistance, diligence, elegance, and ingenuity are available today")
         elif current_day == 'Saturday':
            await ctx.send(f"Today is {current_day} and ballad, gold, light, and praxis are available today")
         elif current_day == 'Sunday':
            await ctx.send(f"Today is {current_day} and everything is available today")
    
    
    @bot.command()
    async def character(ctx, name):
         URL = f'https://api.genshin.dev/characters/{name}'
         img =  f'https://api.genshin.dev/characters/{name}/gacha-splash'
         card = f'https://api.genshin.dev/characters/{name}/icon'
         r = requests.get(URL)
         res = r.json()
         charname = res['name']
         vision = res['vision']
         title = res['title']
         description = res['description']
         em = discord.Embed(
         colour=discord.Colour.dark_blue(),
         description=f"{description}",
         title=f"{title}"
         )
         em.set_image(url=img)
         em.set_footer(text=f"{vision}")
         em.set_author(name=f"{charname}")

         em.set_thumbnail(url=card)
         
         await ctx.send(embed=em)


    @bot.command()
    async def roll(ctx):
        character_list = [
            'albedo',
            'aloy',
            'amber',
            'arataki-itto',
            'ayaka',
            'ayato',
            'barbara',
            'beidou',
            'bennett',
            'chongyun',
            'collei',
            'diluc',
            'diona',
            'eula',
            'fischl',
            'ganyu',
            'gorou',
            'hu-tao',
            'jean',
            'kaeya',
            'kazuha',
            'keqing',
            'klee',
            'kokomi',
            'kuki-shinobu',
            'lisa',
            'mona',
            'ningguang',
            'noelle',
            'qiqi',
            'raiden',
            'razor',
            'rosaria',
            'sara',
            'sayu',
            'shenhe',
            'shikanoin-heizou',
            'sucrose',
            'tartaglia',
            'thoma',
            'tighnari',
            'venti',
            'xiangling',
            'xiao',
            'xingqiu',
            'xinyan',
            'yae-miko',
            'yanfei',
            'yelan',
            'yoimiya',
            'yun-jin',
            'zhongli'

        ]
        char = random.choice(character_list)
        URL = f'https://api.genshin.dev/characters/{char}'
        img =  f'https://api.genshin.dev/characters/{char}/gacha-splash'
        r = requests.get(URL)
        res = r.json()
        charname = res['name']
        em = discord.Embed(
            colour=discord.Colour.dark_blue(),
        )
        em.set_image(url=img)
        em.set_author(name=f"{charname}")

        await ctx.send(embed=em)

    


    bot.run(TOKEN)
    