from Games.Utilites.GAME.GAME import *
from BotUtilities import BotVariables
from BotUtilities import BotFunctions

class MULTIPLAYER_GAME(GAME):
    def __init__(self, channel, title):
        super().__init__(title)
        self.channel = channel
        self.status = 'OPEN'
        self.maxPlayers = None
        self.allowInteruptedPlayer = True

        print(self.title)

    def processHowToPlay(self):
        super().processHowToPlay()
        display = (
            f"{'HOW TO PLAY':^42}\n" +
            '-' * BotVariables.emebedDispalyWidth +
            f"\n{'SPLIT=HERE':=^42}\n" +
            '-' * BotVariables.emebedDispalyWidth +
            f"\nReply JOIN to play"
        )
        embed = BotFunctions.createEmbedFromString(self.title, display, False)
        return embed

        