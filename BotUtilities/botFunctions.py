import discord

from BotUtilities import BotVariables

import random

############### GENERAL ########################################################
def createEmbedFromString(title = None, asciiDisplay = None, hasError = False):

    if not hasError:
        embed = discord.Embed(title=title, description=f"```\n{asciiDisplay}\n```", color=discord.Color.green())
    else:
        embed = discord.Embed(title=title, description=f"```\n{asciiDisplay}\n```", color=discord.Color.red())
    
    return embed

############### GAME ########################################################
def getGames():
    return list(BotVariables.gamesMultiplayer.keys()) + list(BotVariables.gamesSinglePlayer.keys())

def findRandomOpenMulitplayerGame(gameTitle):
    gameType = BotVariables.gamesMultiplayer[gameTitle]

    openGames = []
    for game in BotVariables.activeMultiplayerGames.values():
        if(gameType == type(game) and game.status == 'open'):
            openGames.append(game)

    if len(openGames) == 0:
        status = 'close'
        return status, gameType
    
    status = 'open'
    randomIndex = random.randint(0, len(openGames)-1)
    return status, openGames[randomIndex]
