import discord
from discord.ext import commands
from env import env

from BotUtilities import botVariables
from BotUtilities import botFunctions

from Games.MULIPLAYER_GAME.MULTIPLAYER_GAME import *
from Games.SINGLE_PLAYER_GAME.SINGLE_PLAYER_GAME import *


#Set Up Permissions
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True  # Enable message content intent
intents.dm_messages = True
#https://discordpy.readthedocs.io/en/latest/intents.html




#Create instance of GameBot
bot = commands.Bot(command_prefix='!', intents=intents)
# Server Interaction ##############################################

#The bots first actions upon geting online
@bot.event
async def on_ready():
    print('GameBot is ONLINE...')
    print('---------------------------------------')
    #Check if the server currently has Multiplayer channels set-up
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == 'multiplayer-game':
                botVariables.activeGames[channel.id] = MULTIPLAYER_GAME(channel)
        print(f'Current multiplayer games: {botVariables.activeGames}')

#Detect if a multiplayer-game server was created
@bot.event
async def on_guild_channel_create(channel):
    newMuliplayerGame = channel
    if isinstance(channel, discord.TextChannel) and newMuliplayerGame.name == 'muliplayer-game':
        botVariables.activeGames[channel.id] = MULTIPLAYER_GAME(channel)
        print(f"New channel created: {channel.name} (ID: {channel.id})")

#Detect if a multiplayer-game server was deleted
@bot.event
async def on_guild_channel_delete(channel):
    # Check if the channel was in the active list
    if channel.id in list(botVariables.activeGames.keys()):
        del botVariables.activeGames[channel.id]
        print(f"Channel deleted: {channel.name} (ID: {channel.id})")



# Developer Interaction ###########################################
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
        print('Failed to send user available games')#Send to back-rooms

######## Game Interaction ######################################### 


bot.run(env.TOKEN)

