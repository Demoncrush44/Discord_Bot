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
    bot.remove_command('help')

    
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
        URL = 'https://genshin.jmp.blue/materials/talent-book'

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
        praxis = res['praxis']['characters']
        ingenuity = res['ingenuity']['characters']
        admonition = res['admonition']['characters']

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
        praxis_characters=(' , '.join(str(a) for a in praxis))
        ingenuity_characters=(' , '.join(str(a) for a in ingenuity))
        admonition_characters=(' , '.join(str(a) for a in admonition))



        if current_day == 'Monday':
            await ctx.send(f"{freedom_characters} {prosperity_characters} {transience_characters} {admonition_characters} talent materials are available today!")
        elif current_day == 'Tuesday':
            await ctx.send(f"{resistance_characters} {diligence_characters} {elegance_characters} {ingenuity_characters} talent materials are available today!")
        elif current_day == 'Wednesday':
            await ctx.send(f"{ballad_characters} {gold_characters} {light_characters} {praxis_characters} talent materials are available today!")
        elif current_day == 'Thursday':
            await ctx.send(f"{freedom_characters} {prosperity_characters} {transience_characters} {admonition_characters} talent materials are available today!")
        elif current_day == 'Friday':
            await ctx.send(f"{resistance_characters} {diligence_characters} {elegance_characters} {ingenuity_characters} talent materials are available today!")
        elif current_day == 'Saturday':
            await ctx.send(f"{ballad_characters} {gold_characters} {light_characters} {praxis} talent materials are available today!")
        elif current_day == 'Sunday':
            await ctx.send(f"{freedom_characters} {prosperity_characters} {transience_characters} {resistance_characters} {diligence_characters} {elegance_characters} {ballad_characters} {gold_characters} {light_characters} {praxis_characters}  talent materials are available today!")
    

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
        title = res['title']
        em = discord.Embed(
            colour=discord.Colour.dark_blue(),
            title=f"{title}"
        )
        em.set_image(url=img)
        em.set_author(name=f"{charname}")
        
        await ctx.send("You rolled")
        await ctx.send(embed=em)


    @bot.command()
    async def weapon(ctx, name):
        URL = f'https://api.genshin.dev/weapons/{name}'
        img =  f'https://api.genshin.dev/weapons/{name}/icon'
        r = requests.get(URL)
        res = r.json()
        weapon_name = res['name']
        type = res['type']
        base_attack = res['baseAttack']
        sub_stat = res['subStat']
        passive_name = res['passiveName']
        passive_desc = res['passiveDesc']
        em = discord.Embed(
            colour=discord.Colour.yellow(),
            title=f"{type}"
            )
        em.set_author(name=f"{weapon_name}")
        em.set_thumbnail(url=img)
        em.add_field(name="Base Attack", value=f"{base_attack}", inline=False)
        em.add_field(name="Sub Stat", value=f"{sub_stat}", inline=False)
        em.add_field(name=f"{passive_name}", value=f"{passive_desc}", inline=False)
    
            
        await ctx.send(embed=em)
    

    @bot.command()
    async def artifact(ctx, name):
        URL = f'https://api.genshin.dev/artifacts/{name}'
        random_artifacts = [
            'circlet-of-logos',
            'flower-of-life',
            'goblet-of-eonothem',
            'plume-of-death',
            'sands-of-eon'

        ]
        artifact = random.choice(random_artifacts)
        img = f'https://api.genshin.dev/artifacts/{name}/{artifact}'
        r = requests.get(URL)
        res = r.json()
        artifact_name = res['name']
        two_piece = res['2-piece_bonus']
        four_piece = res['4-piece_bonus']

        em = discord.Embed(
            colour=discord.Colour.yellow()
            )
        em.set_author(name=f"{artifact_name}")
        em.set_image(url=img)
        em.add_field(name="Two-piece", value=f"{two_piece}", inline=False)
        em.add_field(name="Four-piece", value=f"{four_piece}", inline=False)

        await ctx.send(embed=em)
    

    @bot.command()
    async def enemy(ctx, name):
        URL = f'https://genshin.jmp.blue/enemies/{name}'
        img = f'https://genshin.jmp.blue/enemies/{name}/portrait'
        thumbnail = f'https://genshin.jmp.blue/enemies/{name}/icon'
        r = requests.get(URL)
        res = r.json()
        enemy_name = res['name']
        description = res['description']
        region = res['region']

        em = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=f'{enemy_name}'
        )
        em.set_image(url=img)
        em.set_thumbnail(url=thumbnail)
        em.add_field(name="*Entry*", value=f"**{description}**", inline=False)
        em.set_footer(text = f'{region}')

        await ctx.send(embed=em)

   


    @bot.command()
    async def help(ctx):
        em = discord.Embed(color=0x0080ff, title="Commands")
        em.add_field(name="Roll", value="Roll a random character", inline=False)
        em.add_field(name="Talent", value="Get today's talent materials", inline=False)
        em.add_field(name="Character (name)", value="learn about your favorite characters", inline=False)
        em.add_field(name="CV", value="Calculate your artifacts crit values", inline=False)
        em.add_field(name="CT", value="Shows which characters talents are available today", inline=False)
        em.add_field(name="Weapon (name)", value="Shows weapon details", inline=False)
        em.add_field(name="Enemy (name)", value="Shows enemy details", inline=False)
        await ctx.send(embed=em)
    


    bot.run(TOKEN)
    