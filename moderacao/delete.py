import discord
from discord import app_commands
from discord.ext import commands

class Delete(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()  
    async def delete(self, ctx, quantidade: int):
        await ctx.channel.purge(limit=quantidade)
        await ctx.send(f"{quantidade} mensagens apagadas!", delete_after=5)

async def setup(client):
    await client.add_cog(Delete(client))
