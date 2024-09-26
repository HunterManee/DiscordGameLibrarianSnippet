import discord

from BotUtilities import BotVariables

import random

############### GENERAL ########################################################
def createEmbedFromString(title = None, display = None, hasError = False):

    if not hasError:
        embed = discord.Embed(title=title, description=f"```\n{display}\n```", color=discord.Color.green())
    else:
        embed = discord.Embed(title=title, description=f"```\n{display}\n```", color=discord.Color.red())
    
    return embed

############### GAME ########################################################
def getGames():
    return list(BotVariables.gamesMultiplayer.keys()) + list(BotVariables.gamesSinglePlayer.keys())


def findRandomOpenPublicMultiplayerGameChannel(gameTitle):
    gameType = BotVariables.gamesMultiplayer[gameTitle]

    openChannels = []
    for channel in list(BotVariables.activeArcadeChannels.keys()):
        if (BotVariables.activeArcadeChannels[channel] == gameType and 
             BotVariables.activeArcadeChannels[channel].status == 'OPEN'):
            openChannels.append(channel)
    if len(openChannels) == 0:
        return None

    openPublicChannels = []
    for channel in openChannels:
        everyoneRole = channel.guild.default_role
        permissions = channel.permission_for(everyoneRole)
        if not(permissions.view_channel): #check if channel is private
            continue

        openPublicChannels.append(channel)

    if len(openPublicChannels) == 0:
        return None

    randomIndex = random.randint(0, len(openPublicChannels) - 1)
    selectedChannel = openPublicChannels[randomIndex]
    return selectedChannel
