import os
import discord
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}がDiscordに接続しました！')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hi'):
        await message.add_reaction('🙌')

client.run(TOKEN)