#  MCBot_Main.py
#  main entry point for the Moon CommandBot
#--------------------------------------------------------------------------
import asyncio
import sys
try:
    from discord.ext import commands
    from discord.ext.commands import Bot
    from discord import Game
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
from utils import globals
import MCBot

global properties
extensions = ['admin', 'custom_trello', 'trello_wrapper']

globals.init("config.json")
globals.properties.discord_bot = MCBot(command_prefix=globals.properties.bot_prefix, prefix=globals.properties.bot_prefix)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        properties.discord_bot.load_extension(f"cogs.{name}")

properties.discord_bot.run(properties.discord_tk)
