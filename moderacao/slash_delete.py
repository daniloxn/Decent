import discord
from discord import app_commands
from discord.ext import commands

class SlashDelete(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="delete", description="Apaga mensagens do chat.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def slash_delete(self, interaction: discord.Interaction, amount: int):
        """Comando para apagar mensagens no chat."""
        
        if interaction.channel is None:
            await interaction.response.send_message("❌ Não consegui acessar este canal.", ephemeral=True)
            return

        # ⚠️ Deferir resposta para evitar erro de timeout
        await interaction.response.defer()

        # Apagar mensagens
        deleted = await interaction.channel.purge(limit=amount)

        # Enviar resposta editada após deletar mensagens
        await interaction.followup.send(f"✅ {len(deleted)} mensagens apagadas!")


    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.slash_delete)
        self.client.tree.sync()

async def setup(client):
    await client.add_cog(SlashDelete(client))
