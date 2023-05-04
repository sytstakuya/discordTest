#!/usr/bin/env python3
import discord
import time 
import datetime
import os

# 適宜置き換えて下さい
TOKEN = os.getenv("DISCORD_TOKEN")
MESSAGE_ID = 111111

intents = discord.Intents.none()
intents.reactions = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

# リアクションが追加された時の処理
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id != MESSAGE_ID:
        return
    global t_add
    t_add = time.time()
    diff = t_add - t_remove
    func(diff)

# リアクションが削除された時の処理
@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != MESSAGE_ID:
        return
    global t_remove
    t_remove = time.time()

# リアクションが削除された時間と追加された時間の書き出し
def func(diff):
    dt = datetime.datetime.now()
    f = open("./time.log","a")
    f.write("logout:" + str(dt - datetime.timedelta(seconds=diff)) + "\n")
    f.write("login :" + str(dt) + "\n")
    f.close()

client.run(TOKEN)