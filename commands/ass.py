import discord
import requests
from discord.ext import commands

def Image():
    url = "https://hmtai.hatsunia.cfd/v2/ass"
    response = requests.get(url)
    data = response.json()
    image = data['url']

    return image


class Ass(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def asss(self, ctx):
        embed = discord.Embed(
            title="Eita lapa de bundão"
        )
        embed.set_image(url=Image())

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Ass(client))