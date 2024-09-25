from BotUtilities.BotCommands.ChannelCommand import *

class DMChannel(ChannelCommand):
    def __init__(self, user, location):
        super().__init__(user, location)
        self.commands = [ #ALL CAP COMMANDS

        ]

    def processCommand(self, userInput):
        location, embed = super().processCommand(userInput)
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from DMChannel.py...')
        print('-'*42)

