from BotUtilities import BotVariables

############### PONG ###########################################################
def getPong():
    return 'pong'
############### MENU ###########################################################
def getMenu(channel):
    menu = (
            f"{'Available Games To Play':^42}\n"
            f"{'=' * BotVariables.emebedDispalyWidth}\n"
        )
    

    if channel in list(BotVariables.activeArcadeChannels.keys()):
        menu += f"\n{'MULTIPLAYER':-^42}\n"
        for gameTitle in BotVariables.gamesMultiplayer.keys():
            menu += f"{gameTitle:^42}\n"
    elif len(BotVariables.waitingList) > 0:
        menu += f"\n{'MULTIPLAYER':-^42}\n"
        for gameTitle in BotVariables.gamesMultiplayer.keys():
            gameType = BotVariables.gamesMultiplayer[gameTitle]
            if gameType in list(BotVariables.gamesMultiplayer.values()):
                menu += f"{gameTitle:^42}\n"
        
    if len(BotVariables.gamesSinglePlayer) > 0 and channel not in list(BotVariables.activeArcadeChannels.keys()):
        menu += f"\n{'SINGLE-PLAYER':-^42}\n"
        for game in BotVariables.gamesSinglePlayer.keys():
            menu += f"{game:^42}\n"

    print(menu)
    return menu