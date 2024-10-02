import asyncio


class TurnUtilities:
    def __init__(self) :
        self.turnCounter = None

    def __repr__(self):
        return (
            f"Game(turnCounter={self.turnCounter}, "
        )

    #For a countable number of people
    def nextTurn(self):
        self.turnCounter += 1
    
    def prevTurn(self):
        self.turnCounter -= 1

    def resetTurns(self):
        self.turnCounter = 0
    
    def getCurrentTurn(self):
        return self.turnCounter
    
    #For a none countable amount of people
    async def roundMessageCollection(ctx, bot, floatSeconds):
        print('[TurnUtilities.py ln.21]Round Message Collection...')

        collectedMessages = []

        def check(message):
            # Only collect messages from the author in the same channel
            return message.author == ctx.author and message.channel == ctx.channel

        try:
            # Collect messages for 10 seconds
            while True:
                message = await bot.wait_for('message', check=check, timeout=floatSeconds)
                collectedMessages.append(message.content)

        except asyncio.TimeoutError:
            return collectedMessages
    

