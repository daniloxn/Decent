import discord
import requests
import random
from discord.ext import commands
from discord import app_commands


def Porcentagem(arg):
    
    if arg >= 0 and arg <= 24:
        fracasso = [
            "Nem a ciência explica esse desastre. ❌",
            "Isso não é um casal, é um erro estatístico. 💀",
            "Se juntarem, a Terra pode rachar ao meio. 🌍⚡",
            "Não casa nem se for a última pessoa na Terra. 🚷",
            "Fugiria dessa relação mais rápido que a luz. 💨",
            "Se depender desse match, é melhor virar monge. 🧘",
            "Casamento? Só no multiverso da ilusão. 🌌",
            "Esse casal tem a química de óleo e água. 🛢️💧"
        ]
        valor = random.choice(fracasso)
        value = Resultado("nope")
    elif arg >= 25 and arg <= 49:
        talvez = [
            "Dá pra casar, mas com contrato de risco. ⚠️",
            "Tem potencial... Mas é melhor testar antes. 🧐",
            f"50% chance de dar certo, 50% de tragédia. 🎭",
            "O match existe, mas é tipo um bug de sistema. 💻🔧",
            "Se investir muito, talvez funcione... Talvez. 💸",
            "Daria certo? Talvez. Mas já preparou o seguro? 🚑",
            "Precisa de ajustes, mas pode surpreender. 🔧💘",
            "Casal 50/50: pode ser amor ou pode ser guerra. 🔥"
        ]
        valor = random.choice(talvez)
        value = Resultado("smile")
    elif arg >= 50 and arg <= 74:
        bons = [
            "Isso tem futuro! Já podem escolher os padrinhos. 💍",
            "Poderia ser roteiro de comédia romântica. 🎬💖",
            "O match tá aprovado, mas não relaxa ainda! 📜",
            "Não é perfeito, mas dá um casal top. 🔥",
            "Vai render muitos momentos fofos. 😍",
            "A compatibilidade tá forte, só falta um empurrãozinho! 💪",
            "Casamento? Talvez! Filhos? Depende... 👶",
            "A química é boa, só falta aquele empurrão do destino. 🎯"
        ]
        valor = random.choice(bons)
        value = Resultado("dance")
    elif arg >= 75 and arg <= 100:
        perfeito = [
            "Casal perfeito! Até o destino já shippa. 💘",
            "Isso aqui é amor de outra vida! ✨",
            "Se casar, dura até no pós-vida. 👻💍",
            "O tipo de amor que dá inveja nos romances. 📖💞",
            "Casem logo e me convidem pro casamento! 🎊",
            "Alma gêmea detectada com sucesso! ✅",
            "Isso aqui não é casal, é conexão de alma. 🔗💙",
            "Par perfeito! Nem precisa de teste, já tá aprovado. 🎯"
        ]
        valor = random.choice(perfeito)
        value = Resultado("handhold")
        
    return valor, value

def Resultado(arg):
    url = f"https://nekos.best/api/v2/{arg}"
    response = requests.get(url)
    data = response.json()
    image = data['results'][0]["url"]
    return image

class SlashMarry(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="marry", description=f"Vê quantos % de compatibilidade tem os dois usuarios marcados")
    async def marry(self, interaction: discord.Interaction, user1: discord.Member, user2: discord.Member):
        porc = random.randint(0, 101)
        embed = discord.Embed(
            title=Porcentagem(porc)[0],
            description=f"{user1.mention} tem {porc}% de compatibilidade com {user2.mention}"
        )
        embed.set_image(url=Porcentagem(porc)[1])
        await interaction.response.send_message(embed=embed)
        @commands.Cog.listener()
        async def on_ready(self):
            self.client.tree.add_command(self.marry)
            self.client.tree.sync()

async def setup(client):
    await client.add_cog(SlashMarry(client))      