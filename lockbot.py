import discord
from discord.ext import commands
import json
import os

LOCKS_FILE = "locks.json"

# Carregar locks do arquivo, se existir
if os.path.exists(LOCKS_FILE):
    with open(LOCKS_FILE, "r") as f:
        locked_files = json.load(f)
else:
    locked_files = {}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def save_locks():
    with open(LOCKS_FILE, "w") as f:
        json.dump(locked_files, f, indent=4)


def parse_lock_key(key):
    # Suporte para categorias: exemplo BP:Player, MAP:Nivel1
    if ":" in key:
        categoria, nome = key.split(":", 1)
        return categoria.upper(), nome
    return "UNCATEGORIZED", key


@bot.command()
async def lock(ctx, *, arquivo):
    user = ctx.author.name
    categoria, nome = parse_lock_key(arquivo)

    if categoria not in locked_files:
        locked_files[categoria] = {}

    if nome in locked_files[categoria]:
        await ctx.send(f"`{nome}` já está bloqueado por {locked_files[categoria][nome]}.")
    else:
        locked_files[categoria][nome] = user
        save_locks()
        await ctx.send(f"`{nome}` foi bloqueado na categoria [{categoria}] por {user}.")


@bot.command()
async def unlock(ctx, *, arquivo):
    user = ctx.author.name
    categoria, nome = parse_lock_key(arquivo)

    if categoria in locked_files and nome in locked_files[categoria]:
        if locked_files[categoria][nome] == user:
            del locked_files[categoria][nome]
            if not locked_files[categoria]:
                del locked_files[categoria]
            save_locks()
            await ctx.send(f"`{nome}` foi liberado da categoria [{categoria}] por {user}.")
        else:
            await ctx.send(f"Você não pode liberar `{nome}` que está bloqueado por {locked_files[categoria][nome]}.")
    else:
        await ctx.send(f"`{nome}` não está bloqueado.")


@bot.command()
async def locks(ctx):
    if not locked_files:
        await ctx.send("Nenhum arquivo está bloqueado.")
        return

    response = "**Arquivos bloqueados:**\n"
    for categoria, arquivos in locked_files.items():
        response += f"**[{categoria}]**\n"
        for nome, user in arquivos.items():
            response += f"  - `{nome}`: {user}\n"
    await ctx.send(response)


@bot.command()
async def mylocks(ctx):
    user = ctx.author.name
    encontrados = []

    for categoria, arquivos in locked_files.items():
        for nome, dono in arquivos.items():
            if dono == user:
                encontrados.append(f"[{categoria}] `{nome}`")

    if encontrados:
        await ctx.send("Seus arquivos bloqueados:\n" + "\n".join(encontrados))
    else:
        await ctx.send("Você não tem nenhum arquivo bloqueado.")


# Discord Bot token seria aqui, mas estamos usando o env no Railway
bot.run(os.getenv("TOKEN"))
