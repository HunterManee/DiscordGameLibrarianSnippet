from Games.Utilites.GAME.GAME import *
from Games.Utilites.PLAYER.USER import *
from Games.Utilites.PLAYER.BOT import *

class SINGLE_PLAYER_GAME(GAME):
    def __init__(self, user, title):
        super().__init__(title)
        self.user = user
        self.playerDict[user] = USER(user)
        self.playerDict[0] = BOT()