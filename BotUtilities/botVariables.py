from BotUtilities import GameImport

############## DEVELOPER VARIABLES ###############################
prefix = 'Play '
emebedDispalyWidth = 42

channelBackroom = None

############## CHANNEL/GAME VARIABLES ############################
activeGames = {} #(user/channel).id : Game() *ie: SINGLE or MULTI PLAYER GAME object*

activeGameChannels = {} #channel.id : type MULTIPLAY_GAME
waitingList = {} #tyoe MULTIPLAYER_GAME : list(user)


gamesMultiplayer = { 
    'Multiplayer_Game': GameImport.MULTIPLAYER_GAME #Template
}
gamesSinglePlayer = {
    'Single_Player_Game': GameImport.SINGLE_PLAYER_GAME #Template
}


'''
    -arcade allows groups to play a multiplayer game public/private

    -play GAME (ouside arcade): start single or join multi
    -play GAME (inside arcade): Change multiplay game of arcade
    -invite @member (inside arcade):invites member to public/private muliplayer game
'''


