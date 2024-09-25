import discord
from discord.ext import commands
from env import env

from BotUtilities import BotVariables
from BotUtilities import BotFunctions
from BotUtilities import GameImport
from BotUtilities.BotCommands import BotCommand
#ARACADE

#Set Up Permissions
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True  # Enable message content intent
intents.dm_messages = True
#https://discordpy.readthedocs.io/en/latest/intents.html

#Create instance of GameBot
bot = commands.Bot(command_prefix=BotVariables.prefix, intents=intents)

# Server Interaction ##############################################
@bot.event
async def on_ready():
    print('GameBot is ONLINE...')
    print('=======================================')
    for guild in bot.guilds:
        # Search through all channels in the guild
        for channel in guild.channels:
            if channel.name == 'arcade':
                BotVariables.activeGameChannels[channel.id] = GameImport.MULTIPLAYER_GAME

# Channel Interaction #############################################
@bot.event
async def on_guild_channel_create(channel):
    if not(channel.name == 'arcade'):
        return
    #A channel named arcade has been created
    BotVariables.activeGameChannels[channel.id] = GameImport.MULTIPLAYER_GAME
    print(f'activeGameChannels={BotVariables.activeGameChannels}')
    print('-'*42)

@bot.event
async def on_guild_channel_update(before, after):
    if before.name == after.name:
        return
    #If the channel name changed to arcade
    if after.name == 'arcade':
        #and the channel is already in the active game channels
        if after.id in list(BotVariables.activeGameChannels.keys()):
            return
        #If the channel isn't already an active game channel then add it
        BotVariables.activeGameChannels[after.id] = GameImport.MULTIPLAYER_GAME

    print(f'activeGameChannels={BotVariables.activeGameChannels}')
    print('-'*42)

@bot.event
async def on_guild_channel_delete(channel):
    #If the channel is not in the active game channels
    if channel.id not in list(BotVariables.activeGameChannels.keys()):
        return
    #Deleted channel from active game channels
    del BotVariables.activeGameChannels[channel.id] 
    print(f'activeGameChannels={BotVariables.activeGameChannels}')

    #If the channel does not have an active game playing
    if channel.id not in list(BotVariables.activeGames.keys()):
        print('-'*42)
        return
    #Delete the active game playing if the active game channel was deleted
    del BotVariables.activeGames[channel.id] #Multiplayer and single player
    print(f'activeGames={BotVariables.activeGames}')
    print('-'*42)

# Command Interaction #############################################
@bot.event
async def on_message(message):
    user = message.author

    if user == bot.user:
        return
    #The message is not from this bot
    messageChannel = message.channel
    userInput = message.content
    
    #If the channel is a dm channel
    if isinstance(messageChannel, discord.DMChannel):
        BotCommand.DMChannel
        await bot.process_commands(message)
        return
    
    #If the channel is not a text channel
    if not(isinstance(messageChannel, discord.TextChannel)):
        return

    #if channel is a non arcade channel
    if messageChannel.id not in list(BotVariables.activeGameChannels.keys()):
        await bot.process_commands(message)
        return

    #Channel is an arcade channel

    await bot.process_commands(message)

# Developer Interaction ###########################################
@bot.command()
async def ping(ctx):#when the user sends the message: !hello
    await ctx.send('pong')

# User Interaction ################################################
@bot.command()
async def games(ctx):
    embed = BotFunctions.getMainMenuEmbed()
    try:
        await ctx.send(embed=embed)
    except:
        print('---------------------------------------')
        print('Failed to send user available games')#Send to back-rooms
        print('---------------------------------------')


bot.run(env.TOKEN)

