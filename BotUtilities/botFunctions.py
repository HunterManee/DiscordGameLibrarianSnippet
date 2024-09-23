import discord
from BotUtilities import botVariables

def createEmbedFromString(title = None, asciiDisplay = None, hasError = False):

    if not hasError:
        embed = discord.Embed(title=title, description=f"```\n{asciiDisplay}\n```", color=discord.Color.green())
    else:
        embed = discord.Embed(title=title, description=f"```\n{asciiDisplay}\n```", color=discord.Color.red())
    
    return embed

def getMainMenuEmbed():
    title = ''
    asciiGameList = (
            f"{'Available Games To Play':^42}\n"
            f"{'=' * botVariables.emebedDispalyWidth}\n"
        )
    
    if len(botVariables.gamesMultiplayer) > 0:
        asciiGameList += f"\n{'MULTIPLAYER':-^42}\n"
        for game in botVariables.gamesMultiplayer:
            asciiGameList += f"{game:^42}\n"

    
    if len(botVariables.gamesSinglePlayer) > 0:
        asciiGameList += f"\n{'SINGLE-PLAYER':-^42}\n"
        for game in botVariables.gamesSinglePlayer:
            asciiGameList += f"{game:^42}\n"
    
    embed = createEmbedFromString(title, asciiGameList)
    return embed