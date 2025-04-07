import discord
from discord.ext import commands
from discord import app_commands
import json

# Cogの定義：Botの機能を分けて書ける
class KagerouInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # JSONファイルから団員データを読み込む
        with open("data/members.json", encoding="utf-8") as f:
            self.members = json.load(f)

    # /member
    @app_commands.command(name="member", description="指定した団員の情報を表示します")
    @app_commands.describe(name="団員の名前（例: キド）")
    async def member_info(self, interaction: discord.Interaction, name: str):
       name_lower = name.lower()

        # 入力された名前がデータにあるかチェック(aliases対応)
       for member_data in self.members.values():
        if name_lower in [alias.lower() for alias in member_data.get("aliases",[])]:
            #正式名称取得(JSON内の"name")
            official_name = member_data["name"]
            
            # カラーを文字列 "#xxxxxx" から int に変換
            color_hex = member_data.get("color", "#6e4aff")
            color_int = int(color_hex.lstrip("#"), 16)

            # Embedで綺麗に表示
            embed = discord.Embed(title=f"{name}の情報", color=color_int)
            embed.add_field(name="団員No", value=member_data["団員No"], inline=False)
            embed.add_field(name="紹介", value=member_data["紹介"], inline=False)
            embed.add_field(name="能力", value=member_data["能力"], inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f"{name}は見つかりませんでした。", ephemeral=True)

# この関数が main 側の load_extension() で呼ばれる
async def setup(bot):
    await bot.add_cog(KagerouInfo(bot))
