import discord
from discord.ext import commands
from env import env

from BotUtilities import BotVariables
from BotUtilities import BotFunctions
from BotUtilities.BotCommands import ChannelImports
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
    print('ArcadeBot is ONLINE...')
    print('=======================================')
    for guild in bot.guilds:
        # Search through all channels in the guild
        for channel in guild.channels:
            if channel.name == 'arcade':
                BotVariables.activeArcadeDisplays[channel] = None
                continue

            if channel.name == 'backroom':
                BotVariables.channelBackroom = channel
                continue
        for member in guild.members:
            if member.bot and member.name in list(BotVariables.botContacts.keys()):
                BotVariables.botContacts[member.name] = member

        print(BotVariables.botContacts)

@bot.event
async def on_member_join(member):
    if member.bot and member.name not in list(BotVariables.botContacts.keys()):
        BotVariables.botContacts[member.name] = member

# Channel Interaction #############################################
@bot.event
async def on_guild_channel_create(channel):

    #A channel named arcade has been created
    if channel.name == 'arcade':       
        BotVariables.activeArcadeDisplays[channel] = None
        print(f'activeArcadeDisplays={BotVariables.activeArcadeDisplays}')
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
        if after in list(BotVariables.activeArcadeDisplays.keys()):
            return
        #If the channel isn't already an active game channel then add it
        BotVariables.activeArcadeDisplays[after] = None

    if after.name == 'backroom':
        BotVariables.channelBackroom = after
    elif before.name == 'backroom':
        BotVariables.channelBackroom = None

    print(f'activeArcadeDisplays={BotVariables.activeArcadeDisplays}')
    print('-'*42)

@bot.event
async def on_guild_channel_delete(channel):

    if channel.name == 'backroom':
        BotVariables.channelBackroom = None
        return

    #If the channel is not in the active game channels
    if channel not in list(BotVariables.activeArcadeDisplays.keys()):
        return

    #Deleted channel from active game channels
    del BotVariables.activeArcadeDisplays[channel] 
    print(f'activeArcadeDisplays={BotVariables.activeArcadeDisplays}')

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
    user = message.author
    # if user == bot.user:
    #     return
    #The message is not from this bot
    messageChannel = message.channel
    try:
        if bot.user == user: #If this bot is sending messages
            await ChannelImports.BotChannel(bot, messageChannel).processMessage(message)
            return

        #If the channel is a dm channel
        if isinstance(messageChannel, discord.DMChannel):
            location, embed = await ChannelImports.DMChannel(user, messageChannel).processCommand(message)
            await location.send(embed=embed)
            return
        
        elif isinstance(messageChannel, discord.TextChannel):

            #if channel is a non arcade channel
            if messageChannel not in list(BotVariables.activeArcadeDisplays.keys()):
                location, embed = await ChannelImports.Channel(user, messageChannel).processCommand(message)
                await location.send(embed=embed)
                return

            #Channel is an arcade channel
            location, embed = ChannelImports.ArcadeChannel(user, messageChannel).processCommand(message)
            await location.send(embed=embed)
    except discord.Forbidden:
        print('discord')
        return
    except AttributeError:
        print('attribute')
        return

bot.run(env.TOKEN)

