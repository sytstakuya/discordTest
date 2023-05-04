import discord
import os

intents = discord.Intents.none()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

# Bot が所属しているチャンネルにメッセージがされた時に動作する処理
# プライベートチャンネルを用意しそこに Bot を追加している
@client.event
async def on_message(msg):
# メッセージのチャンネルがプライベートチャンネルに該当しない場合
# メッセージを無視する
    txt_channel = client.get_channel(CHANNEL_ID)
    if txt_channel != msg.channel:
        return
# メッセージの内容が "test" の場合削除する
    if msg.content == "test":
        await msg.delete()
# 特定のメッセージの状態取得
    message = await txt_channel.fetch_message(MESSAGE_ID)
    emoji = "👍"
# 1度のみ実行
    if get_flag():
        global member
        id = MEMBER_ID
        member = await message.guild.fetch_member(id)
# リアクションの有無に応じてリアクションの追加/削除を行う
    if not message.reactions:
        await message.add_reaction(emoji)
    else:
        await message.remove_reaction(emoji,member)

# 初回の呼び出し時のみ True を返しそれ以降は False を返す
def get_flag():
    global get_flag
    def get_flag():
        return False
    return True
    
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID"))
MEMBER_ID = int(os.getenv("MEMBER_ID"))
client.run(TOKEN)