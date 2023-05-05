import os
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

# TARGET_CHANNELS = [int(os.getenv("CHANNEL_ID_1")), int(os.getenv("CHANNEL_ID_2"))]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # print(f'message {message}')
    if message.author.bot:
        return

    if message.content == "/自己紹介":

        # サーバーからロールを取得
        male_role = discord.utils.get(message.guild.roles, name='男性')
        female_role = discord.utils.get(message.guild.roles, name='女性')

        channel_id = ''

        # 実行者が「男性」もしくは「女性」ロールを持っているか確認
        if male_role in message.author.roles:
            channel_id = int(os.environ.get("CHANNEL_ID_MALE"))
            await message.channel.send("あなたは男性です")
        elif female_role in message.author.roles:
            channel_id = int(os.environ.get("CHANNEL_ID_FEMALE"))
            await message.channel.send("あなたは女性です")
        else:
            await message.channel.send("あなたの性別は不明です")
            return

        # 環境変数からチャンネルIDを取得
        channel1_id = int(os.environ.get("CHANNEL_ID_1"))
        channel2_id = int(os.environ.get("CHANNEL_ID_2"))
        
        # メッセージを投稿したチャンネルの取得
        channel = message.channel
        
        # 指定された2つのチャンネルから投稿を検索する
        for target_channel_id in [channel1_id, channel2_id]:
            target_channel = client.get_channel(target_channel_id)
            async for msg in target_channel.history(limit=100):
                if msg.author == message.author:
                    # 投稿が見つかった場合、再投稿する
                    await channel.send(f"{msg.content} (by {msg.author.name})")
                    return
        
        # 投稿が見つからなかった場合、過去の投稿を検索する
        async for msg in channel.history(limit=100):
            if msg.author == message.author:
                await channel.send(f"{msg.content} (by {msg.author.name})")
                return

        # メッセージが見つからなかった場合
        await channel.send("自己紹介が見つかりませんでした")

client.run(os.getenv("DISCORD_TOKEN"))