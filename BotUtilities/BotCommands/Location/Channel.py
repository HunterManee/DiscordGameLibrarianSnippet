from BotUtilities.BotCommands.ChannelCommand import *

class Channel(ChannelCommand):
    def __init__(self, user, location):
        super().__init__(user, location)
        self.commands = [ #ALL CAP COMMANDS

        ]

    def processCommand(self, userInput):
        location, embed = super().processCommand(userInput)
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from Channel.py...')
        print('-'*42)

        titleMultiplayer = userInput in list(BotVariables.gamesMultiplayer.keys())
        titleSinglePlayer = userInput in list(BotVariables.gamesSinglePlayer.keys())
        command = userInput in self.commands

        if titleMultiplayer:
            return None

        if titleSinglePlayer:
            return None

        if command:
            return None


        



