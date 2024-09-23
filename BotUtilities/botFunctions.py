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
    for game in botVariables.gameList:
        asciiGameList += f"{game:^42}\n"
    embed = createEmbedFromString(title, asciiGameList)
    return embed