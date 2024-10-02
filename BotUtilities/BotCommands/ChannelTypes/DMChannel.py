from BotUtilities.BotCommands.ChannelCommand import *


class DMChannel(ChannelCommand):
    def __init__(self, user, channel):
        super().__init__(user, channel)
        self.commands = [ #ALL CAP COMMANDS

        ]

    async def processCommand(self, message):
        location, embed = super().processCommand(message, self.user)
        print(f'location={location}, embed={embed}')
        userInput = message.content
        if not(embed == None):#If user input is default command
            print('-'*42)
            return location, embed
        print('processing COMMAND from DMChannel.py...')
        print('-'*42)

        titleGame = userInput in list(BotVariables.gameDict.keys())
        command = userInput in self.commands

        if titleGame:
            return None, None

        if command:
            return None, None
