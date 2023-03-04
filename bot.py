import discord
from discord.ext import commands
from assets import *
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


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None


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
            await ctx.send(f"{ballad_characters} {gold_characters} {light_characters} {praxis_characters} talent materials are available today!")
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
        URL = f'https://genshin.jmp.blue/characters/{name}'
        img =  f'https://genshin.jmp.blue/characters/{name}/gacha-splash'
        card = f'https://genshin.jmp.blue/characters/{name}/icon-big'
        r = requests.get(URL)
        res = r.json()
        charname = res['name']
        vision = res['vision']
        title = res['title']
        description = res['description']
        rarity = res['rarity']
        weapon = res['weapon']
        nation = res['nation']
        affiliation = res['affiliation']
        birthday = res['birthday']
        constellation = res['constellation']
        
        a = birthday.split('-')
        birthday_format = ('-'.join(a[1:]))


         
        em = discord.Embed(
         colour=discord.Colour.dark_blue(),
         description=f"{description}",
         title=f"{title}"
         )
        em.set_author(name=f"{charname}")
        em.set_thumbnail(url=card)

        em.add_field(
            name='**__Character Info__**',
            value='\u200b',     
            inline=False
        )
         
        if charname in male_characters:
            em.add_field(
                name="Gender",
                value=':male_sign:Male',
                inline=True
            )
        else:
            em.add_field(
                name="Gender",
                value=':female_sign:Female',
                inline=True
            )
             
        em.add_field(
             name="Nation",
             value=f':mailbox_closed:{nation}',
             inline=True
         )

        em.add_field(
             name="Affiliation",
             value=f':tophat:{affiliation}',
             inline=True
         )

        em.add_field(
             name="Weapon",
             value=f':dagger:{weapon}',
             inline=True
         )
        if vision == 'Geo':
             em.add_field(
             name="Vision",
             value=f':mountain:{vision}',
             inline=True
         )
        elif vision == 'Cryo':
             em.add_field(
             name="Vision",
             value=f':snowflake:{vision}',
             inline=True
         )
        elif vision == "Pyro":
             em.add_field(
             name="Vision",
             value=f':fire:{vision}',
             inline=True
         )
        elif vision == "Hydro":
             em.add_field(
             name="Vision",
             value=f':bubbles:{vision}',
             inline=True
         )
        elif vision == "Dendro":
             em.add_field(
             name="Vision",
             value=f':deciduous_tree:{vision}',
             inline=True
         )
             
        elif vision == "Electro":
             em.add_field(
             name="Vision",
             value=f':zap:{vision}',
             inline=True
         )
             
        elif vision == "Anemo":
             em.add_field(
             name="Vision",
             value=f':cloud_tornado:{vision}',
             inline=True
         ) 
                    
        em.add_field(
               name=":birthday:Birthday",
               value=f'{birthday_format}',
               inline=True
        )

        em.add_field(
                name='Constellation',
                value=f':comet:{constellation}',
                inline=True
        )


        if charname in standard_banner:
            em.add_field(
                name="Obtained",
                value=":fireworks:Standard banner",
                inline=True
            )
        elif charname in given_characters:
            em.add_field(
                name="Obtained",
                value=":fireworks:Given/Standard Banner",
                inline=True
            )
        elif charname in travler_element:
            em.add_field(
                name="Obtained",
                value=":fireworks:Statue of Sevens",
                inline=True
            )
        else:
            em.add_field(
                name="Obtained",
                value=":fireworks:Event Banner",
                inline=True
            )


        if rarity == 5:
             em.add_field(
                 name="Rarity",
                 value=':star::star::star::star::star:',
                 inline=True
             )
        elif rarity == 4:
            em.add_field(
                name="Rarity",
                value=':star::star::star::star:',
                inline=True
                 )

        
        view = Menu()
        view.add_item(discord.ui.Button(label="Portrait", style=discord.ButtonStyle.red, url=img))
        

        await ctx.send(embed=em, view=view)


    @bot.command()
    async def roll(ctx, n):
        for _ in range(n):
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
        URL = f'https://genshin.jmp.blue/weapons/{name}'
        img =  f'https://genshin.jmp.blue/weapons/{name}/icon'
        r = requests.get(URL)
        res = r.json()
        weapon_name = res['name']
        type = res['type']
        base_attack = res['baseAttack']
        sub_stat = res['subStat']
        passive_name = res['passiveName']
        passive_desc = res['passiveDesc']
        location = res['location']
        material = res.get('ascensionMaterials') or None
        rarity = res['rarity']



        em = discord.Embed(
            colour=discord.Colour.yellow(),
            title=f"{passive_name}",
            description=f'{passive_desc}'
            )
        em.set_author(
            name=f'{weapon_name}'
        )

        em.add_field(
            name='*__Weapon Info__*',
            value='\u200b',
            inline=False
        )

        em.add_field(
            name=':crossed_swords:Base Attack',
            value=f'{base_attack}',
            inline=True
        )

        em.add_field(
            name=':axe:Sub Stat',
            value=f'{sub_stat}',
            inline=True
        )

        em.add_field(
            name=f':dagger:Type',
            value=f'{type}',
            inline=True
        )


        if material == None:
            em.add_field(
                name=':pick:Materials',
                value='Not available',
                inline=True
        )
        else:
            em.add_field(
                name=':pick:Materials',
                value=f'{material}',
                inline=True
        )

        em.add_field(
            name=':comet:Obtained',
            value=f'{location}',
            inline=True
        )

        if rarity == 5:
             em.add_field(
                 name="Rarity",
                 value=':star::star::star::star::star:',
                 inline=True
             )
        elif rarity == 4:
            em.add_field(
                name="Rarity",
                value=':star::star::star::star:',
                inline=True
            )
        else:
             em.add_field(
                name="Rarity",
                value=':star::star::star:',
                inline=True
            )

        


        em.set_thumbnail(url=img)
            
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
        rarity = res['max_rarity']

        em = discord.Embed(
            colour=discord.Colour.yellow()
            )
        em.set_author(name=f"{artifact_name}")
        em.set_thumbnail(url=img)
        em.add_field(
            name='*__Artifact Info__*',
            value='\u200b',
            inline=False
        )
        if rarity == 5:
            em.add_field(
                name='Rarity',
                value=':star::star::star::star::star:',
                inline=False
            )
        elif rarity == 4:
            em.add_field(
                name='Rarity',
                value=':star::star::star::star:',
                inline=False
            )
        else:
            em.add_field(
                name='Rarity',
                value=':star::star::star:',
                inline=False
            )



        em.add_field(
                name=':two:Two-piece',
                value=f"{two_piece}", 
                inline=False
        )

        em.add_field(
                name=':four:Four-piece', 
                value=f"{four_piece}", 
                inline=False
        )

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
        type = res['type'] 
        drops = res.get('drops')[0].get('name') or None
        family = res['family']
        elements = res['elements']
        faction = res.get('faction') or None
        element_list=(' | '.join(str(i) for i in elements))
        

        em = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=f'{enemy_name}',
            description=f"{description}"
        )
        em.set_thumbnail(url=thumbnail)
        
        em.add_field(
            name='**__Enemy Info__**',
            value='\u200b',     
            inline=False
        )
        
        if faction == None:
            em.add_field(
            name=':boom:Faction',
            value='Not Available',     
            inline=True
        )
        else:
            em.add_field(
            name=':boom:Faction',
            value=f'{faction}',
            inline=True 
        )    
          
        

        em.add_field(
            name=':triangular_flag_on_post:Region',
            value=f"{region}",
            inline=True
        )

        em.add_field(
            name=":pirate_flag:Enemy-Type",
            value=f"{type}",
            inline=True
        )
        if drops == None:
            em.add_field(
            name=":coin:Drops",
            value='None',
            inline=True
        )
        else:
            em.add_field(
                name=":coin:Drops",
                value=f"{drops}",
                inline=True
        )

        em.add_field(
            name=':family:Family',
            value= f'{family}',
            inline=True
        )
        
        em.add_field(
            name=":stars:Element",
            value= f'{element_list}',
            inline=True
        )




        view = Menu()
        view.add_item(discord.ui.Button(label="Portrait", style=discord.ButtonStyle.red, url=img))
        await ctx.send(embed=em, view=view)
    

    @bot.command()
    async def weekly(ctx, name):
        url = f'https://genshin.jmp.blue/boss%2Fweekly-boss/{name}'
        img = f'https://genshin.jmp.blue/boss%2Fweekly-boss/{name}/icon'
        r = requests.get(url)
        res = r.json()

        boss_name = res['name']
        description = res['description']
        first_drop = res['drops'][0]['name']
        second_drop = res['drops'][1]['name']
        third_drop = res['drops'][2]['name']


        em = discord.Embed(
            colour= discord.Colour.blurple(),
            title=f'{boss_name}',
            description=f'{description}'
        )

        em.set_thumbnail(url=img)

        em.add_field(
            name='**__Enemy Info__**',
            value='\u200b',     
            inline=False
        )

        em.add_field(
            name=':flying_disc:Drop',
            value=f'{first_drop}',
            inline=True

        )

        em.add_field(
            name=':flying_disc:Drop',
            value=f'{second_drop}',
            inline=True

        )

        em.add_field(
            name=':flying_disc:Drop',
            value=f'{third_drop}',
            inline=True

        )

        em.add_field(
            name='Rarity',
            value=':star::star::star::star::star:',
            inline=True
        )

        em.add_field(
            name='Rarity',
            value=':star::star::star::star::star:',
            inline=True
        )

        em.add_field(
            name='Rarity',
            value=':star::star::star::star::star:',
            inline=True
        )

        await ctx.send(embed=em)
   


    @bot.command()
    async def help(ctx):
        em = discord.Embed(color=0x0080ff, title="Commands")
        em.add_field(name="Roll (n)", value="Roll a random character (n) times", inline=False)
        em.add_field(name="Talent", value="Get today's talent materials", inline=False)
        em.add_field(name="Character (name)", value="learn about your favorite characters", inline=False)
        em.add_field(name="CV", value="Calculate your artifacts crit values", inline=False)
        em.add_field(name="CT", value="Shows which characters talents are available today", inline=False)
        em.add_field(name="Weapon (name)", value="Shows weapon details", inline=False)
        em.add_field(name="Enemy (name)", value="Shows enemy details", inline=False)
        em.add_field(name="Weekly (name)", value="Shows boss details", inline=False)
        await ctx.send(embed=em)
    


    bot.run(TOKEN)
    