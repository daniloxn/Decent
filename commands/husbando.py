from discord.ext import commands
import discord
import random
import mysql.connector

class Husbando(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.used_ids_man = set()  # Agora está corretamente inicializado no __init__

    def Ha(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                database='descent',
                user='root',
                password=''
            )

            cursor = conexao.cursor()
            cursor.execute("SELECT id FROM fem_pers;")
            ids_disponiveis = [row[0] for row in cursor.fetchall()]

            if not ids_disponiveis:
                return None
            
            if len(self.used_ids_man) >= len(ids_disponiveis):
                self.used_ids_man.clear()

            ids_restantes = list(set(ids_disponiveis) - self.used_ids_man)
            rnd_id = random.choice(ids_restantes)

            self.used_ids_man.add(rnd_id)

            cursor.execute("SELECT nome, anime, image FROM man_pers WHERE id = %s", (rnd_id,))
            result = cursor.fetchone()

            cursor.close()
            conexao.close()

            return result
        
        except mysql.connector.Error as err:
            print(f"Erro no bando de dado: {err}")
            return None
        
    @commands.command()
    async def ha(self, ctx):
        husband_data = self.Ha()

        if not husband_data:
            await ctx.send("Nenhum husband disponível no momento! 😭")
            return
        
        nome, anime, img = husband_data

        embed = discord.Embed(
            title=nome,
            description=anime,
            colour=0xFFC0CB
        )

        embed.set_image(url=img)
        embed.set_footer(text="Provide by `descent`", icon_url="https://i.pinimg.com/736x/71/65/d4/7165d489402cbbf7138189ddf57ab3ad.jpg")

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Husbando(client))


    

