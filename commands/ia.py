import discord
from discord.ext import commands
import pathlib
import textwrap
import google.generativeai as genai
GOOGLE_API_KEY="AIzaSyAaNw5gknrUC3pHX9PnT3Rb7YuNiHNH6zs"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
def Resposta(*args):
    response = chat.send_message(args)
    return response.text
    

class Ia(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ia(self, ctx, *, arg):
        await ctx.send(f"{Resposta(arg)}")

async def setup(client):
    await client.add_cog(Ia(client))
