import discord
from discord import Client
from discord import Intents
import random
import inspirobot

# Constants
PREFIX = 'h!'
TOKEN = 'YOUR-TOKEN'

class HonigBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.quote = inspirobot.generate()

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        # Ignore own messages
        if message.author == self.user:
            return

        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = "DM" if isinstance(message.channel, discord.DMChannel) else str(message.channel.name)
        
        print(f'{username}: {user_message} ({channel})')

        # Commands
        if user_message.lower() == 'hello honigism':
            await message.channel.send(f'Hey! {message.author.mention}')
            
        elif user_message.lower() == f'{PREFIX}randomnum':
            await message.channel.send(str(random.randrange(1000)))
            
        elif user_message.lower() == f'{PREFIX}inspire':
            try:
                quote = inspirobot.generate()
                await message.channel.send(quote.url)
            except Exception as e:
                await message.channel.send("Sorry, couldn't generate a quote right now.")
            
        elif user_message.lower() == '727':
            await message.channel.send('https://pbs.twimg.com/media/FXspvhcUUAAN6Pq?format=png&name=large')

if __name__ == '__main__':
    bot = HonigBot()
    bot.run(TOKEN)