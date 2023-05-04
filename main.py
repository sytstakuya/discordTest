import os
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

TARGET_CHANNELS = [int(os.getenv("CHANNEL_ID_1")), int(os.getenv("CHANNEL_ID_2"))]

@client.event
async def on_message(message):
    if message.content == "/自己紹介":
        channel = message.channel
        author = message.author
        
        for channel_id in TARGET_CHANNELS:
            target_channel = client.get_channel(channel_id)
            messages = await target_channel.history(limit=500).flatten()
            for msg in messages:
                if msg.author == author:
                    await channel.send(f"{author.mention} さんの自己紹介です！\n{msg.content}")
                    return
        
        # 見つからなかった場合、最大500件まで過去の投稿を検索する
        for channel_id in TARGET_CHANNELS:
            target_channel = client.get_channel(channel_id)
            messages = await target_channel.history(limit=500).flatten()
            for msg in messages:
                if msg.author == author:
                    await channel.send(f"{author.mention} さんの自己紹介です！\n{msg.content}")
                    return
        
        # どちらも見つからなかった場合
        await channel.send(f"{author.mention} さんの自己紹介は見つかりませんでした...")

client.run(os.getenv("DISCORD_TOKEN"))