import discord
import requests
from discord.ext import commands
from discord import app_commands


def Image():
    url = "https://hmtai.hatsunia.cfd/v2/ass"
    response = requests.get(url)
    data = response.json()
    img = data['url']
    return img


def no():
    # Pega uma imagem de negação
    url = "https://nekos.best/api/v2/nope"
    response = requests.get(url)
    data = response.json()
    img = data['results'][0]['url']

    return img

class SlashAss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ass", nsfw=True, description="Mostra um bundão")
    async def ass(self, interaction: discord.Interaction):
        cargo = "Nsfw"
        if discord.utils.get(interaction.user.roles, name=cargo):
            embed = discord.Embed(
            )

            embed.set_image(url=Image())
            embed.set_footer(text="Provide by `hmtai`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            print(f"{interaction.user} ass")
        else:
            embed = discord.Embed(
            description="Você não tem permissão de usar este comando."
            )
            embed.set_image(url=no())
            await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.ass)
        await self.client.tree.sync()

async def setup(client):
   await client.add_cog(SlashAss(client))

