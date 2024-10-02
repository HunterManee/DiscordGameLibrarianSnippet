import discord

from BotUtilities import BotVariables

############### GENERAL ########################################################
def createEmbedFromString(title = None, display = None, hasError = False):

    if not hasError:
        embed = discord.Embed(title=title, description=f"```\n{display}\n```", color=discord.Color.orange())
    else:
        embed = discord.Embed(title=title, description=f"```\n{display}\n```", color=discord.Color.red())
    
    return embed

def validateGameId(gameId):
    for GameId in list(BotVariables.activeGames.keys()):
        if gameId == GameId:
            return True
    return False

def addActiveDisplay(user, message):
    dictLength = len(BotVariables.activePlayerDisplays[user])
    BotVariables.activePlayerDisplays[user] = {str(dictLength) : message}

############### GAME ########################################################

