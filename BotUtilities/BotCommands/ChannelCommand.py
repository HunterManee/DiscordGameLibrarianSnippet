from BotUtilities import BotVariables
from BotUtilities import BotFunctions
from BotUtilities import BotDisplays

from Games.Utilites.PLAYER.USER import *


class ChannelCommand:
    def __init__(self, user, channel):
        self.user = user
        self.channel = channel
        self.Commands = ([
            f'PING',
            f'MENU'
        ])

    def processCommand(self, message):
        userInput = message.content.upper()
        print('processing COMMAND from Command.py..')
        #if userInput is not a base command return None
        if userInput not in self.Commands:
            return None, None

        location = None
        display = ''
        if userInput == self.Commands[0]: #ping
            location = self.channel
            display = BotDisplays.getPong()
        elif userInput == self.Commands[1]: #menu
            location = self.channel
            display = BotDisplays.getMenu(self.channel)
        
        embed = BotFunctions.createEmbedFromString(None, display, False)
        return location, embed
    
    def joinGame(self, gameTitle):
        display = ''
        GameType = BotVariables.gamesMultiplayer[gameTitle]
        arcadeChannel = BotFunctions.findRandomOpenPublicMultiplayerGameChannel(gameTitle) 
        if arcadeChannel == None:
            
            for gameType in BotVariables.waitingList.keys():
                for user in list(BotVariables.waitingList[gameType]):
                    if self.user.id == user.id:
                        #Can only wait for one multiplayer game at a time
                        return None, None

            #New user being added to waiting list
            BotVariables.waitingList[GameType].append(self.user)

            display += 'You are now on the waiting list'
            embed = BotFunctions.createEmbedFromString(None, display)
            #Inform user of being added to waiting list
            return self.channel, embed
        
        #If arcade channel is open
        for userId in list(BotVariables.activeGames[arcadeChannel].playerDict.keys()):
            if self.user.id == userId:
                #user can not be a player in the current arcade game channel
                return None, None
    
        #New Player being added to player dict
        BotVariables.activeGames[arcadeChannel].playerDict[self.user.id] = USER(self.user)

        if (len(BotVariables.activeGames[arcadeChannel].playerDict) >= 
                BotVariables.activeGames[arcadeChannel].maxPlayers):
            BotVariables.activeGames[arcadeChannel].status = 'CLOSE'

        display += 'You will be added into the next round of play'
        embed = BotFunctions.createEmbedFromString(None, display)
        return self.channel, embed

    