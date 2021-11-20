from discord.ext import commands
from os import getenv
import traceback
import discord

client = discord.Client()
TEXT_CHANNEL = 880453619802050620
DND_CHANNEL = 889433349951733770

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(TEXT_CHANNEL)

        # 入室通知（画面共有に反応しないように分岐）
        if after.channel is not None and after.channel is not before.channel:
            if before.channel is None:
                if after.channel.id != DND_CHANNEL:
                    await botRoom.send( member.name + " が参加しました！")
        if after.channel is None:
            await botRoom.send("ボイチャに誰もいなくなりました")
            
token = getenv('DISCORD_BOT_TOKEN')
client.run(token)

