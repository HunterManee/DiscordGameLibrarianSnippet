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

############### MENU ###########################################################
def getMainMenuEmbed():
    title = ''
    asciiGameList = (
            f"{'Available Games To Play':^42}\n"
            f"{'=' * BotVariables.emebedDispalyWidth}\n"
        )
    
    if len(BotVariables.gamesMultiplayer) > 0:
        asciiGameList += f"\n{'MULTIPLAYER':-^42}\n"
        for game in BotVariables.gamesMultiplayer.keys():
            asciiGameList += f"{game:^42}\n"

    
    if len(BotVariables.gamesSinglePlayer) > 0:
        asciiGameList += f"\n{'SINGLE-PLAYER':-^42}\n"
        for game in BotVariables.gamesSinglePlayer.keys():
            asciiGameList += f"{game:^42}\n"
    
    embed = createEmbedFromString(title, asciiGameList)
    return embed

############### GAME ########################################################
def validateGame(gameTitle):
    games = list(BotVariables.gamesSinglePlayer.keys()) + list(BotVariables.gamesMultiplayer.keys())
    if games.count(gameTitle) > 0:
        return f'SUCCESS: {gameTitle} was found'
    return f'LogicERROR: {gameTitle} was not found' 
    

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
