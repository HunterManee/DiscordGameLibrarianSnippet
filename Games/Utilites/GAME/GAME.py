
class GAME:
    def __init__(self, title):
        # self.playerList = []
        self.title = title
        self.playerDict = {} #user/bot : User()/Bot()
        self.turnCounter = None

    def __repr__(self):
        return (f"Game(playerDict={self.playerDict}, "
                f"turnCounter={self.turnCounter}")
    
    def processHowToPlay(self):
        print('[GAME.py ln.12]HOW TO PLAY...')
        return None

    def proccessCommand(self, userInput):
        print(f'[GAME.py ln.16]{userInput} COMMAND...')
        return None

    def processSetup(self, userInput):
        print('[GAME.py ln.20]SETTING UP GAME...')
        return None
    
    def processGame(self, userInput):
        print('[GAME.py ln.24]PROCESSING GAME...')
        return None
    
    def processEnd(self):
        print('[GAME.py ln.12]PROCESSING END OF GAME...')
        return None

