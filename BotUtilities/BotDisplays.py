from BotUtilities import BotVariables
import discord

############### PONG ###########################################################
def getPong():
    return 'pong'
############### MENU ###########################################################
def getMenu():
    menu = (
            f"{'Available Games To Play:'}\n\n"
        )
    
    for gameTitle in list(BotVariables.gameDict.keys()):
        menu += f'{gameTitle}\n'

    return menu