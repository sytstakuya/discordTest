import os
import discord
from dotenv import load_dotenv

load_dotenv()

# インテントの設定
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# discord.pyの初期化
client = discord.Client(intents=intents)

# メッセージ送信イベントをキャッチ
@client.event
async def on_message(message):
    # 投稿者がボットの場合終了
    if message.author.bot:
        return

    # 発火条件(/自己紹介と投稿されたとき)
    if message.content == '/自己紹介':

        # サーバーからロールを取得
        male_role = discord.utils.get(message.guild.roles, name='男性')
        female_role = discord.utils.get(message.guild.roles, name='女性')

        channel_id = ''

        # 実行者が「男性」もしくは「女性」ロールを持っているか確認
        if male_role in message.author.roles:
            channel_id = int(os.environ.get('CHANNEL_ID_MALE'))
        elif female_role in message.author.roles:
            channel_id = int(os.environ.get('CHANNEL_ID_FEMALE'))
        else:
            await channel.send('先に性別のロールを取得してください')
            return

        # 対象の自己紹介チャンネルを取得
        self_introduction_channel = client.get_channel(channel_id)
        async for msg in self_introduction_channel.history(limit=100):
            if msg.author == message.author:
                # 投稿が見つかった場合、再投稿する
                await channel.send(f'{msg.content} (by {msg.author.name})')
                return

        # メッセージが見つからなかった場合
        await channel.send('自己紹介が見つかりませんでした')

# 実行
client.run(os.getenv('DISCORD_TOKEN'))