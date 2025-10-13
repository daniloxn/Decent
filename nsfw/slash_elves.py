import discord
from discord import app_commands
import requests
from discord.ext import commands


def Image():
    url = "https://hmtai.hatsunia.cfd/v2/elves"
    response = requests.get(url)
    data = response.json()
    image = data['url']

    return image

def no():
    # Pega uma imagem de negação
    url = "https://nekos.best/api/v2/nope"
    response = requests.get(url)
    data = response.json()
    img = data['results'][0]['url']

    return img

class SlashElves(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="elves", description="Envia uma imagem de elves")
    async def elves(self, interaction: discord.Interaction):
        cargo = "Nsfw"
        if discord.utils.get(interaction.user.roles, name=cargo):
            embed = discord.Embed(
            )
            embed.set_image(url=Image())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(
            description="Você não tem permissão de usar este comando."
            )
            embed.set_image(url=no())
            await interaction.response.send_message(embed=embed)
    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.elves)
        self.client.tree.sync()

async def setup(client):
    await client.add_cog(SlashElves(client))