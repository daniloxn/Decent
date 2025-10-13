import discord
from discord.ext import commands
import requests

def img():
    url = "https://nekos.best/api/v2/hug"
    response = requests.get(url)
    data = response.json()
    image = data['results'][0]['url']

    return image

class HugView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Retribuir", style=discord.ButtonStyle.blurple)
    async def retribuir(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        embed = discord.Embed(
            description=f"{interaction.user.mention} Retribuiu o abraço",
            colour=0xFF1493
        )
        embed.set_image(url=img())
        embed.set_footer(text="Provide by `nekos.best`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")

        await interaction.response.send_message(embed=embed)


class Hug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, member: discord.Member):

        embed = discord.Embed(
            description=f"{ctx.author.mention} Abraçou {member.mention}",
            colour=0xFF1493
        )
        embed.set_image(url=img())
        embed.set_footer(text="Provide by `nekos.best`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")

        view = HugView()

        await ctx.send(embed=embed, view=view)

async def setup(client):
    await client.add_cog(Hug(client))