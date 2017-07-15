import discord
from discord.ext import commands
import logging
import asyncio

bot = commands.Bot(command_prefix="$")

@bot.command()
async def Hello():
    await bot.say("Hello world!")

@bot.command()
async def Hail():
    await bot.say("Hail Hydra!")

@bot.command()
async def Help():
    await bot.say("Yea you look like a guy who needs help")  

@bot.command()
async def prices():
    await bot.say("""Carbon:     **10** <:Bux:329395951003369476>|      **200K** <:Gas:329395933949198337> |    **850K** <:Minerals:329395908901076992>
Scrap:      **12** <:Bux:329395951003369476>|      **300K** <:Gas:329395933949198337> | **850K-1M** <:Minerals:329395908901076992>
Silicon: **25-30** <:Bux:329395951003369476>|      **500K** <:Gas:329395933949198337> |      **1M** <:Minerals:329395908901076992>
Titanium: **9-12** <:Bux:329395951003369476>|      **250K** <:Gas:329395933949198337> |    **850K** <:Minerals:329395908901076992>
Gold:       **20** <:Bux:329395951003369476>|*Undetermined* <:Gas:329395933949198337> | **850K-1M** <:Minerals:329395908901076992>""")

@bot.command()
async def Retro():
    await bot.say("The snazziest Phoenix in H.Y.D.R.A. <:Retro:333100617470050304>")

@bot.command()
async def RedButton():
    await bot.say("<@&326822888227209216> **HELP!!!**")

@bot.command()
async def pet():
    await bot.say("*You quietly pet <@!243565320571322368>*")

@bot.command()
async def Spanks():
    await bot.say("Hard spanks for Mizz :wink: ")

@bot.command()
async def Dak():
    await bot.say("You'll not find anyone more needy or annoying in the entire universe")

@bot.command()
async def Hydra():
    await bot.say("The most fiersome group of Captains in the known verse")

@bot.command()
async def Ion():
    await bot.say("""https://vignette1.wikia.nocookie.net/pixelstarships/images/3/33/IonCannon2.gif/revision/latest?cb=20170331011041
```A slow yet powerful charge weapon. Causes devastating damage to target.

The Ion Cannon is a powerful weapon that takes a singificant amount of time to charge and consumes an Ion Core for each volley. The Ion Cannon is available for construction on Level 11 starships.```""")

@bot.command()
async def test():
    await bot.say("""```
This
is a test
of fancy multiline
responses```""")

@bot.command()
async def party():
    await bot.say("PARTY BITCHES @everyone")

bot.run("MzM1MjE5NTEzNzEwNjA4Mzg1.DEnGxA.rMsrZ3fmdyqoA2tCdOyjd1IM6Pk")
