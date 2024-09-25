from BotUtilities import BotVariables

############### MENU ###########################################################
def getMenu():
    menu = (
            f"{'Available Games To Play':^42}\n"
            f"{'=' * BotVariables.emebedDispalyWidth}\n"
        )
    
    if len(BotVariables.activeGameChannels) > 0:
        menu += f"\n{'MULTIPLAYER':-^42}\n"
        for game in BotVariables.gamesMultiplayer.keys():
            menu += f"{game:^42}\n"

    
    if len(BotVariables.gamesSinglePlayer) > 0:
        menu += f"\n{'SINGLE-PLAYER':-^42}\n"
        for game in BotVariables.gamesSinglePlayer.keys():
            menu += f"{game:^42}\n"

    return menu

def getPong():
    return 'pong'