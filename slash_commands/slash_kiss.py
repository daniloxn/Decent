from discord.ext import commands
import discord
from discord import app_commands
import requests

def image():
    try:   
        # Pega uma imagem de beijo 
        url = "https://nekos.best/api/v2/kiss"
        response = requests.get(url)
        data = response.json()
        img = data['results'][0]['url']
        nome = data['results'][0]['anime_name']

        return nome, img

    except:
        print("Ocorreu um erro!")
def slap():
        # Pegando uma imagem de tapa
        url = "https://nekos.best/api/v2/slap"
        response = requests.get(url)
        data = response.json()
        img = data['results'][0]['url']

        return img

def no():
    # Pega uma imagem de negação
    url = "https://nekos.best/api/v2/nope"
    response = requests.get(url)
    data = response.json()
    img = data['results'][0]['url']

    return img

    
    
# Class para a criação de uma embed button
class KissView(discord.ui.View):
    def __init__(self, author_id: int, target_id: int):
        super().__init__()
        # Adicionando variaveis para pegar o valor ID
        self.author_id = author_id
        self.target_id = target_id

    # Criando o botão para Retribuir o beijo
    @discord.ui.button(label="Retribuir", style=discord.ButtonStyle.blurple)
    async def retribuir(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Verificando se a pessoa que apertou o botão foi a mesma pessoa que "recebeu o beijo"
        if interaction.user.id != self.target_id:
            # Envia uma mensagem avisando que somente quem foi mencionado pode retribuir
            embed = discord.Embed(
                title="Apenas a pessoa que recebeu o beijo pode retribuir ",
                colour=0xFF1493
            )
            embed.set_image(url=no())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            # Retribuindo o beijo
            embed = discord.Embed(
                description=f"{interaction.user.mention} retribuiu o beijo 💋"
            )
            embed.set_image(url=image()[1])
            embed.set_footer(text="Provide by `nekos.best`")
            await interaction.response.send_message(embed=embed)

    # Criando o botão para negar o beijo
    @discord.ui.button(label="Negar", style=discord.ButtonStyle.red)
    async def negar(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Verificando se a pessoa que apertou o botão foi a mesma pessoa que foi mencionada
        if interaction.user.id != self.target_id:
            embed = discord.Embed(
                title="Apenas a pessoa que recebeu o beijo pode negar ",
                colour=0xFF1493
            )

            await interaction.response.send_message(embed=embed)
        else:
            # Nega o beijo
            embed = discord.Embed(
                description=f"{interaction.user.mention} Negou o beijo",
                color= discord.Color.red()
            )

            embed.set_image(url=slap())
            embed.set_footer(text="Provide by `nekos.best`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")
            await interaction.response.send_message(embed=embed)
    # Cria um botão que retorna o nome do anime da imagem 
    @discord.ui.button(label='Fonte da Imagem', emoji="🖼️")
    async def fonte(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"{image()[0]}", ephemeral=True)
# Criando uma class para armazena o comando
class SlashKiss(commands.Cog):
    def __init__(self, client):
        self.client = client

    # criando o comando slash para "beijar" outro usuário
    @app_commands.command(name="kiss", description="Beija o usuario marcado")
    async def kiss(self, interaction: discord.Interaction, member: discord.Member):
        # Tenta pegar o valor da função image()
        try:
            image()
        except:
            # Caso não consiga, avisa ao usuário que não foi possivel 
            await interaction.response.send_message("Não foi possivel dar beijoquinhas. 😭")
            return
        # Criando uma Embed
        embed = discord.Embed(
            description=f"{interaction.user.mention} Beijou {member.mention}",
            color=discord.Color.purple()
        )
        # Setando imagem da Embed
        embed.set_image(url=image()[1])
        embed.set_footer(text="Provide by `nekos.best`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")
        view = KissView(interaction.user.id, member.id)
        await interaction.response.send_message(embed=embed, view=view)
        
    # Criando um evento para semrpe que o bot estiver online, adicionar o comando ao bot
    @commands.Cog.listener()
    async def on_ready(self):
        self.client.tree.add_command(self.kiss)
        await self.client.tree.sync()
    



async def setup(client):
    await client.add_cog(SlashKiss(client))

