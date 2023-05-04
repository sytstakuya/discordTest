#!/usr/bin/env python3
import discord
import time
import os

# 適宜置き換えて下さい
# TOKEN = 'YourAccessToken'
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 11111111

intents = discord.Intents.none()
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')
    channel = client.get_channel(CHANNEL_ID)
    while True:
        await channel.send("test")
        time.sleep(2)
    
client.run(TOKEN)