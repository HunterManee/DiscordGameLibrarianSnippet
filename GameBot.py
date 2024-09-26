import discord
from discord.ext import commands
from env import env

from BotUtilities import BotVariables
from BotUtilities import BotFunctions
from Games import GameImport
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
bot = commands.Bot(command_prefix='!', intents=intents)

# Server Interaction ##############################################
@bot.event
async def on_ready():
    print('GameBot is ONLINE...')
    print('=======================================')
    for guild in bot.guilds:
        # Search through all channels in the guild
        for channel in guild.channels:
            if channel.name == 'arcade':
                BotVariables.activeArcadeChannels[channel] = None
                continue

            if channel.name == 'backroom':
                BotVariables.channelBackroom = channel
                continue

# Channel Interaction #############################################
@bot.event
async def on_guild_channel_create(channel):

    #A channel named arcade has been created
    if channel.name == 'arcade':       
        BotVariables.activeArcadeChannels[channel] = None
        print(f'activeArcadeChannels={BotVariables.activeArcadeChannels}')
        print('-'*42)
        return
    
    #A channel named backroom has been created
    if channel.name == 'backroom':
        BotVariables.channelBackroom = channel
        print(f'backroom={BotVariables.channelBackroom}')
        print('-'*42)
        return

@bot.event
async def on_guild_channel_update(before, after):
    if before.name == after.name:
        return

    #If the channel name changed to arcade
    if after.name == 'arcade':
        #and the channel is already in the active game channels
        if after.id in list(BotVariables.activeArcadeChannels.keys()):
            return
        #If the channel isn't already an active game channel then add it
        BotVariables.activeArcadeChannels[after.id] = None

    if after.name == 'backroom':
        BotVariables.channelBackroom = after
    elif before.name == 'backroom':
        BotVariables.channelBackroom = None

    print(f'activeArcadeChannels={BotVariables.activeArcadeChannels}')
    print('-'*42)

@bot.event
async def on_guild_channel_delete(channel):

    if channel.name == 'backroom':
        BotVariables.channelBackroom = None
        return

    #If the channel is not in the active game channels
    if channel not in list(BotVariables.activeArcadeChannels.keys()):
        return
    
    gameType = BotVariables.activeArcadeChannels[channel]
    if list(BotVariables.activeArcadeChannels.values()).count(gameType) == 1 and gameType != None:
        del BotVariables.waitingList[gameType]

    #Deleted channel from active game channels
    del BotVariables.activeArcadeChannels[channel] 
    print(f'activeArcadeChannels={BotVariables.activeArcadeChannels}')

    #If the channel does not have an active game playing
    if channel not in list(BotVariables.activeGames.keys()):
        print('-'*42)
        return

    #Delete the active game playing if the active game channel was deleted
    del BotVariables.activeGames[channel] #Multiplayer and single player
    print(f'activeGames={BotVariables.activeGames}')
    print('-'*42)

# Command Interaction #############################################
@bot.event
async def on_message(message):
    newMessage = message
    user = message.author
    print(user)
    # if user == bot.user:
    #     return
    #The message is not from this bot
    messageChannel = message.channel
    try:

        #If the channel is a dm channel
        if isinstance(messageChannel, discord.DMChannel):
            location, embed = BotCommand.DMChannel(user, messageChannel).processCommand(newMessage)
            await location.send(embed=embed)
            await bot.process_commands(message)
            return
        
        
        if isinstance(messageChannel, discord.TextChannel):

            #if channel is a non arcade channel
            if messageChannel not in list(BotVariables.activeArcadeChannels.keys()):
                location, embed = BotCommand.Channel(user, messageChannel).processCommand(newMessage)
                await location.send(embed=embed)
                await bot.process_commands(message)
                return

            #Channel is an arcade channel
            location, embed = BotCommand.ArcadeChannel(user, messageChannel).processCommand(newMessage)
            await location.send(embed=embed)
            await bot.process_commands(message)

    except:
        await bot.process_commands(message)

bot.run(env.TOKEN)

