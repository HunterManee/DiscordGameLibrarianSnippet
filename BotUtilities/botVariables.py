from Games import GameImport

############## DEVELOPER VARIABLES ###############################
prefix = 'PLAY '
emebedDispalyWidth = 42

channelBackroom = None

############## CHANNEL/GAME VARIABLES ############################
activeGames = {} #user/channel : Game() *ie: SINGLE or MULTI PLAYER GAME object*

activeArcadeChannels = {} #channel : type MULTIPLAYER_GAME
waitingList = {} #tyoe MULTIPLAYER_GAME : list(user)


gamesMultiplayer = { 
    'Multiplayer_Game': GameImport.MULTIPLAYER_GAME #Template
}
gamesSinglePlayer = {
    'Single_Player_Game': GameImport.SINGLE_PLAYER_GAME #Template
}



