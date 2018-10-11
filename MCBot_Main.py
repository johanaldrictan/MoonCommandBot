#  MCBot_Main.py
#  main entry point for the Moon CommandBot
#--------------------------------------------------------------------------
import asyncio
try:
    from discord.ext import commands
    from discord.ext.commands import Bot
    from discord import Game
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
from utils import globals

global properties
extensions = ['admin', 'custom_trello', 'trello_wrapper']

init("config.json")
properties.discord_bot = MCBot(command_prefix=properties.bot_prefix, prefix=properties.bot_prefix)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

properties.discord_bot.run(properties.discord_tk)
