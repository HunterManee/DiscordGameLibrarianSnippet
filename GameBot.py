import discord
from discord.ext import commands
from env import env

from BotUtilities import botVariables
from BotUtilities import botFunctions

#Set Up Permissions
intents = discord.Intents.default()
#https://discordpy.readthedocs.io/en/latest/intents.html


#Create instance of GameBot
bot = commands.Bot(command_prefix='!', intents=intents)

# Developer Interaction ###########################################
@bot.event
async def on_ready():
    print('GameBot is ONLINE...')
    print('---------------------------------------')

@bot.command()
async def ping(ctx):#when the user sends the message: !hello
    await ctx.send('pong')

# User Interaction ################################################
@bot.command()
async def games(ctx):
    embed = botFunctions.getMainMenuEmbed()
    try:
        await ctx.send(embed=embed)
    except:
        print('Failed to send user available games')

######## Game Interaction ######################################### 


bot.run(env.TOKEN)

