#  MCBot_Main.py
#  main entry point for the Moon CommandBot
#  Author: Johan Tan
#--------------------------------------------------------------------------
import requests
import aiohttp
import asyncio
import sys
import time
import json
try:
    from discord.ext import commands
    from discord.ext.commands import Bot
    from discord import Game
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
try:
    from trello import TrelloClient
except ImportError:
    print("py-trello.py is not installed.\n")
    sys.exit(1)

args = sys.argv[1:]
BOT_PREFIX = "MC!"
DISCORD_TK = args[2];
API_TK = args[0];
API_KY = args[1];
channel = ""

client = Bot(command_prefix=BOT_PREFIX)
trello_client = TrelloClient(
    api_key=API_KY,
    token=API_TK
)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name=''))
    print("Logged in as " + client.user.name)

@client.command(name="assign",
                description="Assigns bot to the current channel the command is on.")
async def assign(message):
    global channel
    channel = message.channel
    await client.message(channel, "")

@client.command(name="token",
                description="Supplies the user a link to determine the token that the bot will use.")
async def token():
    await client.message(channel,"Not implemented yet")
@client.command(name="link",
                description="Links the bot to the trello account with the correct token")
async def link():
    await client.message(channel,"Not implemented yet")
@client.command(name="ping",
                description='Tests bot connectivity to Trello')
async def ping():
    start = time.time()
    boards = trello_client.list_boards()
    end = time.time()
    embed = discord.Embed(title="Pong!", description="Time elapsed " + (end - start) + "seconds", color="f0efc8")
    await client.message(channel,embed=embed)


@client.command(name="logout")
async def logout():
    await client.message(channel,"Logging out.")
    await client.logout()

async def message(message):
    #if channel is unassigned, use the regular channel
    if(channel == ""):
        await client.say(message)
    else:
        await client.message()
client.run(DISCORD_TK)
