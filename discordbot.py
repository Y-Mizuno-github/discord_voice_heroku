from discord.ext import commands
from os import getenv
import traceback
import discord

bot = commands.Bot(command_prefix='/')
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(TEXT_ID)

        # 入室通知（画面共有に反応しないように分岐）
        if after.channel is not None and after.channel is not before.channel:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
