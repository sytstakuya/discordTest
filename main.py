import logging
logging.basicConfig(level=logging.INFO)

import os
import discord
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1103731669275525313

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    print(f"Message received: {message.content}, Channel: {message.channel.id}")
    # if message.content == '/hi' and message.channel.id == CHANNEL_ID:
        await message.add_reaction('🙌')

client.run(TOKEN)
