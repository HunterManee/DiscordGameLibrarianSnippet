from BotUtilities.BotCommands.Command import *

class ArcadeChannel(Command):
    def __init__(self):
        super().__init__()
        self.Commands = [ #ALL CAP COMMANDS

        ]

    def processCommand(self, userInput):
        super().processCommand(userInput)
        print('processing COMMAND from ArcadeChannel.py...')
        print('-'*42)
