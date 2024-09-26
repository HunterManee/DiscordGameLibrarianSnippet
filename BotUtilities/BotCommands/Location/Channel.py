from BotUtilities.BotCommands.ChannelCommand import *


class Channel(ChannelCommand):
    def __init__(self, user, channel):
        super().__init__(user, channel)
        self.commands = [ #ALL CAP COMMANDS

        ]

    def processCommand(self, message):
        location, embed = super().processCommand(message)
        userInput = message.content
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from Channel.py...')
        print('-'*42)

        titleMultiplayer = userInput in list(BotVariables.gamesMultiplayer.keys())
        titleSinglePlayer = userInput in list(BotVariables.gamesSinglePlayer.keys())
        command = userInput in self.commands

        if titleMultiplayer:
            self.joinGame()
            arcadeChannel = BotFunctions.findRandomOpenPublicMultiplayerGameChannel(userInput)
            if arcadeChannel == None:
                display = f'No {userInput} games are available'
                embed = BotFunctions.createEmbedFromString(None, display, False)
                return self.channel, embed

        if titleSinglePlayer:
            return None, None

        if command:
            userInput = userInput.upper()
            return None, None


        



