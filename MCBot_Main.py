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
DISCORD_TK = args[1];
API_KY = args[0];
channel = ""
color = 0xf0efc8

client = Bot(command_prefix=BOT_PREFIX)
trello_client = ""

@client.event
async def on_ready():
    await client.change_presence(game=Game(name=''))
    print("Logged in as " + client.user.name)

@client.command(name="assign",
                description="Assigns bot to the current channel the command is on.",
                pass_context = True)
async def assign(ctx):
    global channel
    channel = ctx.message.channel
    await message("Assigned to " + str(ctx.message.channel.name))

@client.command(name="token",
                description="Supplies the user a link to determine the token that the bot will use.")
async def token():
    await message("https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Moon%20CommandBot&key="+API_KY)
@client.command(name="link",
                description="Links the bot to the trello account with the correct token")
async def link(api_token):
    global API_TK
    API_TK = api_token
    global trello_client
    trello_client = TrelloClient(
        api_key=API_KY,
        token=API_TK
    )
    await message("Received token of Token: " + API_TK)
@client.command(name="ping",
                description='Tests bot connectivity to Trello')
async def ping():
    if(check_trello()):
        start = time.time()
        boards = trello_client.list_boards()
        end = time.time()
        embed = discord.Embed(title="Pong!", description="Time elapsed {time:3f} seconds".format(time=(end-start)), color=color)
        await send_embed(embed)
    else:
        embed = discord.Embed(title="Error!", description="Trello client not connected. Please use MC!token and MC!link to connect the trello to the bot.", color=color)
        await send_embed(embed)

@client.command(name="logout")
async def logout():
    await message("Logging out.")
    print("Logging out.")
    await client.logout()

async def message(message):
    #if channel is unassigned, use the regular channel
    if(channel == ""):
        await client.say(message)
    else:
        await client.send_message(channel,message)
async def send_embed(embed):
    #if channel is unassigned, use the regular channel
    if(channel == ""):
        await client.say(embed=embed)
    else:
        await client.send_message(channel,embed=embed)
def check_trello():
    global trello_client
    if(trello_client == ""):
        return False
    else:
        return True
client.run(DISCORD_TK)
