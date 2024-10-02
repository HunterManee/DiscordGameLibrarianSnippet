from Games.Utilites.PLAYER.PLAYER import *

class PLAYER_USER(PLAYER):
    def __init__(self, user):
        super().__init__(user.id)
        self.user = user
