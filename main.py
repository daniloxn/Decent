import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    for file in os.listdir(path="commands"):
        if file.endswith(".py"):
            try:
                await client.load_extension(f'commands.{file[:-3]}')
            except Exception as e:
                print(f"Erro ao carregar {file}: {e}")

    for file in os.listdir(path="slash_commands"):
        if file.endswith(".py"):
            try:
                await client.load_extension(f'slash_commands.{file[:-3]}')
            except Exception as e:
                print(f"Erro ao carregar {file}: {e}")
    for file in os.listdir(path="moderacao"):
        if file.endswith(".py"):
            try:
                await client.load_extension(f'moderacao.{file[:-3]}')
            except Exception as e:
                print(f"Erro ao carregar {file}: {e}")
    try:
        synced = await client.tree.sync()
    except Exception as e:
        print(e)

    print(f"Synced {len(synced)} command(s)")
    print(f"Bot {client.user} está online!")



#client.run(token)
client.run("Seu token")

