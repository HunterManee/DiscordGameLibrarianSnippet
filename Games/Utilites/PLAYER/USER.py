from Games.Utilites.PLAYER.PLAYER import *

class USER(PLAYER):
    def __init__(self, user):
        super().__init__(user.id)
        self.user = user
        self.message = None
