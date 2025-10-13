import discord
from discord.ext import commands
from discord import app_commands
import requests

def hug():
    url = "https://nekos.best/api/v2/hug"
    resp = requests.get(url)
    data = resp.json()
    image = data['results'][0]['url']

    return image

def no():
    # Pega uma imagem de negação
    url = "https://nekos.best/api/v2/nope"
    response = requests.get(url)
    data = response.json()
    img = data['results'][0]['url']

    return img

class HugView(discord.ui.View):
    def __init__(self, author_id: int, target_id: int):
        super().__init__()
        # Adicionando variaveis para pegar o valor ID
        self.target_id = target_id
        self.author_id = author_id


    @discord.ui.button(label="Retribuir",emoji="🥰" , style=discord.ButtonStyle.blurple)
    async def retribuir(self, interaction: discord.Interaction, member: discord.Member):
        if interaction.user.id != self.target_id:
            embed = discord.Embed(
            title="Apenas a pessoa que recebeu o abraço pode retribuir ",
            colour=0xFF1493
            )
            embed.set_image(url=no())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(
                description=f"{interaction.user.mention} Retribuiu o abraço <@{self.author_id}>!.",
                colour=0xFF1493
            )
            embed.set_image(url=hug())

            await interaction.response.send_message(embed=embed)

        
class SlashHug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='hug', description="Abraça o usuário.")
    async def hug_slash(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            description=f"{interaction.user.mention} Abraçou {member.mention}"
        )
        embed.set_image(url=hug())
        embed.set_footer(text="Provide by `nekos.best`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")
        view = HugView(target_id=member.id, author_id=interaction.user.id)
        await interaction.response.send_message(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.hug_slash)
        await self.client.tree.sync()

async def setup(client):
    await client.add_cog(SlashHug(client))
        