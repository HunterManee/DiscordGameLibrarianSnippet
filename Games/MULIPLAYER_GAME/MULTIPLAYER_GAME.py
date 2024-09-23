from Games.Game import *

class MULTIPLAYER_GAME(Game):
    def __init__(self, channel):
        super().__init__(channel, isMultiplayer=True)
        pass