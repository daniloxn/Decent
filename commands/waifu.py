from discord.ext import commands
import discord
from discord import app_commands
import random
import mysql.connector


class Wai(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.used_ids_woman = set()  # Agora está corretamente inicializado no __init__

    def Wai(self):
        try:
            # Fazendo conexão com o banco de dados.
            conexao = mysql.connector.connect(
                host='localhost',
                database='descent',
                user='root',
                password=''
            )
            cursor = conexao.cursor()
            cursor.execute("SELECT id FROM fem_pers;")
            ids_disponiveis = [row[0] for row in cursor.fetchall()]

            # Se não houver IDs disponíveis, retorna None
            if not ids_disponiveis:
                return None

            # Resetando a lista se todos os IDs já foram usados
            if len(self.used_ids_woman) >= len(ids_disponiveis):
                self.used_ids_woman.clear()

            # Pegando um ID aleatório que ainda não foi usado
            ids_restantes = list(set(ids_disponiveis) - self.used_ids_woman)
            rnd_id = random.choice(ids_restantes)

            # Adicionando o ID à lista de usados
            self.used_ids_woman.add(rnd_id)

            # Buscando a waifu correspondente ao ID
            cursor.execute('SELECT nome, anime, image FROM fem_pers WHERE id = %s', (rnd_id,))
            result = cursor.fetchone()

            # Fechando a conexão
            cursor.close()
            conexao.close()

            return result
        except mysql.connector.Error as err:
            print(f"Erro no banco de dados: {err}")
            return None

    @commands.command()
    async def wa(self, ctx):
        waifu_data = self.Wai()  

        if not waifu_data:
            await ctx.send("Nenhuma waifu disponível no momento! 😭")
            return

        nome, anime, img = waifu_data

        # Criando o embed
        embed = discord.Embed(
            title=nome,
            description=anime,
            colour=0xFFC0CB
        )
        embed.set_image(url=img)

        await ctx.send(embed=embed)

        print(f"IDs usados até agora: {self.used_ids_woman}")

    

async def setup(client):
    await client.add_cog(Wai(client))
