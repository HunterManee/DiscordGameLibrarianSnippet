from BotUtilities.Models.GameModel import *

############## DEVELOPER VARIABLES ###############################
prefix = 'PLAY '
emebedDispalyWidth = 42

channelBackroom = None
botContacts = {
    'Mr. Game N. Bot': 'https://discord.com/oauth2/authorize?client_id=1286361688358256711&permissions=8&integration_type=0&scope=bot'
}
############## CHANNEL/GAME VARIABLES ############################
activeGames = dict() #(user/channel)host : list(GAME(title, host))
activePlayerDisplays = dict() #user : { displayName : message }
activeArcadeDisplays = dict() #channel : { displayName : message } 

gameDict = { 
    'GAME_NAME': GameModel('GAME_NAME', None)
}




