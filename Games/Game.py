
class Game:
    def __init__(self, channel, isMultiplayer):
        self.channel = channel
        self.isMultiplayer = isMultiplayer

        self.playerList = []
        self.status = 'open'
