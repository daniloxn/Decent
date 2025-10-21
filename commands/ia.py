import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar chave do .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configurar modelo Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])

# Função de resposta da IA
def Resposta(mensagem: str):
    response = chat.send_message(mensagem)
    return response.text


class Ia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ia(self, ctx, *, arg):
        await ctx.send(Resposta(arg))


async def setup(client):
    await client.add_cog(Ia(client))
