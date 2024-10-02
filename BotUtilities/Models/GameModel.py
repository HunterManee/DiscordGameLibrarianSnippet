
class GameModel:
        #Game must have a built-in transition from single to multi
    def __init__(self, title, host):
        self.title = title
        self.host = host

        self.playerDict = dict() #user/bot : User()/Bot()
        self.maxPlayers = None

    def __repr__(self):
        return ('[GameModel.py Ln.12]:\n'
            f"Game(title={self.title}, "
            f"host={self.host.name}, "
            f"playerDict={self.playerDict}, "
            f"maxPlayers={self.maxPlayers}, "
        )
    
    def processHowToPlay(self):
        print('[GameModel.py ln.21]HOW TO PLAY...')
        return None

    def proccessCommand(self, userInput):
        print(f'[GameModel.py ln.25]{userInput} COMMAND...')
        return None

    def processSetup(self, userInput):
        print('[GameModel.py ln.29]SETTING UP GAME...')
        return None
    
    def processGame(self, userInput):
        print('[GameModel.py ln.33]PROCESSING GAME...')
        return None
    
    def processEnd(self):
        print('[GameModel.py ln.37]PROCESSING END OF GAME...')
        return None