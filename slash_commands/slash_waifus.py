import discord
import requests
from discord.ext import commands
from discord import app_commands

def wai():
    url = "https://nekos.best/api/v2/waifu"
    response = requests.get(url)
    data = response.json()
    img = data['results'][0]["url"]
    
    
    return img



class SlashWaifus(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="waifus", description="Pega uma imagem aleatoria de alguma personagem de anime feminina")
    async def waifus(self, interaction: discord.Interaction):

        embed = discord.Embed(
        )

        embed.set_image(url=wai())

        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.waifus)
        self.client.tree.sync()


async def setup(client):
    await client.add_cog(SlashWaifus(client))