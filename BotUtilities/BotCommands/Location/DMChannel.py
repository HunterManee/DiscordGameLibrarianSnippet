from BotUtilities.BotCommands.ChannelCommand import *

class DMChannel(ChannelCommand):
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
        print('processing COMMAND from DMChannel.py...')
        print('-'*42)

        titleMultiplayer = userInput in list(BotVariables.gamesMultiplayer.keys())
        titleSinglePlayer = userInput in list(BotVariables.gamesSinglePlayer.keys())
        command = userInput in self.commands

        if titleMultiplayer:
            return None, None

        if titleSinglePlayer:
            return None, None

        if command:
            userInput = userInput.upper()
            return None, None
