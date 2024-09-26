from BotUtilities.BotCommands.ChannelCommand import *
from Games.Utilites.PLAYER.USER import *

class ArcadeChannel(ChannelCommand):
    def __init__(self, user, channel):
        super().__init__(user, channel)
        self.commands = [ #ALL CAP COMMANDS
            'JOIN',
            'OPEN',
            'CLOSE'
        ]

    def processCommand(self, message):
        location, embed = super().processCommand(message)
        userInput = message.content
        print('pass')
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from ArcadeChannel.py...')
        print('-'*42)

        titleMultiplayer = userInput in list(BotVariables.gamesMultiplayer.keys())
        command = userInput.upper() in self.commands
        
        if titleMultiplayer:
            newGameType = BotVariables.gamesMultiplayer[userInput]
            self.scrubWaitingList(newGameType)
            newGameInstance = newGameType(self.channel, userInput)
            BotVariables.activeGames[self.channel] = newGameInstance
            BotVariables.activeArcadeChannels[self.channel] = newGameType
            if newGameType not in list(BotVariables.waitingList.keys()):
                BotVariables.waitingList[newGameType] = list()

            embed = newGameInstance.processHowToPlay()
            return self.channel, embed

        if command:
            userInput = userInput.upper()
            if userInput == 'JOIN':
                gameType = BotVariables.activeArcadeChannels[self.channel]
                return self.joinGame(gameType)
            elif userInput == 'OPEN':
                BotVariables.activeGames[self.channel].status = userInput
                embed = BotFunctions.createEmbedFromString(None, 'This channel is now adding new players')
                return self.channel, embed
            elif userInput == 'CLOSE':
                BotVariables.activeGames[self.channel].status = userInput
                embed = BotFunctions.createEmbedFromString(None, 'This channel is no longer adding new players')
                return self.channel, embed

            return None, None
        
    def scrubWaitingList(self, newGameType):
        oldGameType = BotVariables.activeArcadeChannels[self.channel]
        if oldGameType == newGameType or oldGameType == None:
            return
        

        if list(BotVariables.activeArcadeChannels.values()).count(oldGameType) == 1:
            del BotVariables.waitingList[oldGameType]

    def joinGame(self, GameType):
        display = ''

        if BotVariables.activeGames[self.channel].status == 'CLOSE':

            for gameType in BotVariables.waitingList.keys():
                print(BotVariables.waitingList[gameType])
                for user in list(BotVariables.waitingList[gameType]):
                    print(user)
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
        for userId in list(BotVariables.activeGames[self.channel].playerDict.keys()):
            if self.user.id == userId:
                print('return')
                #user can not be a player in the current arcade game channel
                return None, None
    
        #New Player being added to player dict
        BotVariables.activeGames[self.channel].playerDict[self.user.id] = USER(self.user)

        #After adding new player is the playerDict Full?
        if not(BotVariables.activeGames[self.channel].maxPlayers == None):
            if(len(BotVariables.activeGames[self.channel].playerDict) >= 
                BotVariables.activeGames[self.channel].maxPlayers):
                    BotVariables.activeGames[self.channel].status = 'CLOSE'


        display += 'You will be added into the next round of play'
        embed = BotFunctions.createEmbedFromString(None, display, False)
        return self.user, embed

        
        

