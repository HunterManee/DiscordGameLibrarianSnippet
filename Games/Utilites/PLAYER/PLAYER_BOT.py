from Games.Utilites.PLAYER.PLAYER import *

class PLAYER_BOT(PLAYER):
    def __init__(self, botId = None):

        self.id = botId
        if botId == None:
            self.id = 0
        super().__init__(self.id)
        pass