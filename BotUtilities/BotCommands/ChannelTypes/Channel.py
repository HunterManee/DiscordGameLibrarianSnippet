from BotUtilities.BotCommands.ChannelCommand import *


class Channel(ChannelCommand):
    def __init__(self, user, channel):
        super().__init__(user, channel)
        self.commands = [ #ALL CAP COMMANDS

        ]

    async def processCommand(self, message):
        location, embed = super().processCommand(message, self.channel)
        userInput = message.content
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from Channel.py...')
        print('-'*42)

        gameTitle = userInput in list(BotVariables.gameDict.keys())
        command = userInput in self.commands

        if gameTitle:
            return None, None


        if command:
            userInput = userInput.upper()
            return None, None


        



