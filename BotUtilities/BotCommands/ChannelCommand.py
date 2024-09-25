from BotUtilities import BotVariables
from BotUtilities import BotFunctions
from BotUtilities import BotDisplays

class ChannelCommand:
    def __init__(self, user, channel):
        self.user = user
        self.channel = channel
        self.Commands = ([
            f'PING',
            f'MENU'
        ])

    def processCommand(self, userInput):
        print('processing COMMAND from Command.py..')
        #if userInput is not a base command return None
        if userInput not in self.Commands:
            return None

        location = None
        display = ''
        if userInput == self.Commands[0]: #ping
            location = self.channel
            display = BotDisplays.getPong()
        elif userInput == self.Commands[1]: #menu
            print('iin')
            location = self.channel
            display = BotDisplays.getMenu()
        
        embed = BotFunctions.createEmbedFromString(None, display, False)
        return location, embed