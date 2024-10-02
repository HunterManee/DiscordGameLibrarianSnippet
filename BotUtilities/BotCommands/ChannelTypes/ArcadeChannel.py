from BotUtilities.BotCommands.ChannelCommand import *
from Games.Utilites.PLAYER.PLAYER_USER import *

class ArcadeChannel(ChannelCommand):
    def __init__(self,user, channel):
        super().__init__(user, channel)
        self.commands = [ #ALL CAP COMMANDS
            'BEGIN',
        ]

    def processCommand(self, message):
        location, embed = super().processCommand(message, self.channel)
        userInput = message.content
        print('pass')
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from ArcadeChannel.py...')
        print('-'*42)

        gameTitle = userInput in list(BotVariables.gameDict.keys())
        command = userInput.upper() in self.commands
        
        if gameTitle:
            newGameType = BotVariables.gameDict[userInput]
            newGameInstance = newGameType(self.channel, userInput)
            BotVariables.activeGames[self.channel] = newGameInstance

            embed = newGameInstance.processHowToPlay()
            return self.channel, embed

        if command:
            userInput = userInput.upper()
            if userInput == 'BEGIN':
                return None, None

            return None, None
        
        

