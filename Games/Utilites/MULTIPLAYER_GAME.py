from Games.Utilites.GAME import *

class MULTIPLAYER_GAME(GAME):
    def __init__(self, channel):
        super().__init__()
        self.channel = channel
        self.status = 'open'

        self.maxPlayers = 6
    