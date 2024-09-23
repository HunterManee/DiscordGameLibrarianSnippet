from Games.Game import *

class SINGLE_PLAYER_GAME(Game):
    def __init__(self, channel):
        super().__init__(channel, isMultiplayer=False)
        pass