from discord.ext import commands
from os import getenv
import traceback
import discord

client = discord.Client()

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(880453619802050620)

        # 入室通知（画面共有に反応しないように分岐）
        if after.channel is not None and after.channel is not before.channel:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)