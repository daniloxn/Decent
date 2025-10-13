import discord 
from discord import app_commands
from discord.ext import commands

class SlashCasar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="casar", description="Pede um usuário em casamento!")
    async def casar(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"{interaction.response.send_message("O Adm ficou com preguiça de terminar o codigo, cobra ele.")}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.casar)
        self.client.tree.sync()


async def setup(client):
    await client.add_cog(SlashCasar(client))