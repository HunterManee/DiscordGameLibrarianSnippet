from Games.Utilites.GAME import *

class SINGLE_PLAYER_GAME(GAME):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.playerList.append(user) #and Bot