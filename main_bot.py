import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user}としてログインしました")
    try:
        synced = await bot.tree.sync()
        print(f"スラッシュコマンドを同期しました: {len(synced)}個")
    except Exception as e:
        print(e)
   # await on_ready.response.send_message("団員情報を表示中！")　←これはターミナルに表示させるときの処理？

@bot.event
async def on_ready():
    activity = discord.Game(name="団員情報に接続しています") 
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"準備完了！：{bot.user}")

async def main():
    async with bot:
        await bot.load_extension("cogs.kagerou_info")
        await bot.start(TOKEN)
        

import asyncio
asyncio.run(main())
