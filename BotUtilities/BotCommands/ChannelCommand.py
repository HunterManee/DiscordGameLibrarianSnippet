from BotUtilities import BotVariables
from BotUtilities import BotFunctions
from BotUtilities import BotDisplays

from Games.Utilites.PLAYER.PLAYER_USER import *


class ChannelCommand:
    def __init__(self, user, channel):
        self.user = user
        self.channel = channel
        self.Commands = ([
            'PING',
            'MENU'
        ])

    def processCommand(self, message, menuLocation):
        userInput = message.content.upper()
        print('processing COMMAND from Command.py..')
        #if userInput is not a base command return None
        if userInput not in self.Commands:
            return None, None

        location = None
        display = ''
        if userInput == self.Commands[0]: #ping
            location = self.channel
            display = BotDisplays.getPong()
        elif userInput == self.Commands[1]: #menu
            location = menuLocation
            display = BotDisplays.getMenu()
        
        embed = BotFunctions.createEmbedFromString(None, display, False)
        return location, embed

    