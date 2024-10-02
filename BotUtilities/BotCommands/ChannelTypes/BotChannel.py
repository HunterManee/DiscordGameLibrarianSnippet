from BotUtilities.BotCommands.ChannelCommand import *
import discord

class BotChannel():
    def __init__(self, bot, channel):
        self.bot = bot
        self.channel = channel

    async def processMessage(self, message):

        if isinstance(message.channel, discord.DMChannel):
            await self.processDM(message)
            return
        elif isinstance(message.channel, discord.TextChannel):
            if message.channel in list(BotVariables.activeArcadeDisplays.keys()):
                await self.processArcade(message)
                return
            return

    async def processDM(self, message):
        if not(message.embeds):
            if '|' not in message.content:
                return
            contentArray = message.content.split('|')
            user = self.bot.get_user(int(contentArray[0]))
            messageContent = contentArray[1]
            await message.edit(content=messageContent)
            arcadeName = messageContent.split(' ')[0]
            BotVariables.activePlayerDisplays[user][arcadeName] = message
        
        for embed in message.embeds:
            if embed.title == None:
                continue
            if 'DISPLAY' in embed.title:
                validationArray = embed.title.split(' ')
                #multiplayer uses arcade channel single player uses user
                gameChannel = self.bot.get_channel(int(validationArray[0]))
                user = self.bot.get_user(int(validationArray[1]))
                channelName = gameChannel.name if (
                    gameChannel not in list(BotVariables.activePlayerDisplays.keys())
                )else BotVariables.activeGames[gameChannel].title
                await self.updateDisplay(user, channelName, message)
                BotVariables.activePlayerDisplays[user] = {channelName: message}
                newEmbed = BotFunctions.createEmbedFromString(channelName, embed.description.split("```")[1], False)
                await message.edit(embed=newEmbed)

    async def updateDisplay(self, user, channelName, message):
        if user not in list(BotVariables.activePlayerDisplays.keys()):
            BotVariables.activePlayerDisplays[user] = {channelName: message}

        if channelName not in list(BotVariables.activePlayerDisplays[user].keys()):
            BotVariables.activePlayerDisplays[user] = {channelName: message}

        await BotVariables.activePlayerDisplays[user][channelName].delete()
        BotVariables.activePlayerDisplays[user][channelName] = message

    async def processArcade(self, message):
        #Need to add display from arcade into messages
        pass

