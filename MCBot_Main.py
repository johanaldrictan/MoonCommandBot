#  MCBot_Main.py
#  main entry point for the Moon CommandBot
#--------------------------------------------------------------------------
import asyncio
import sys
import os
try:
    from discord.ext import commands
    from discord.ext.commands import Bot
    from discord import Game
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
import MCBot

MCBot = MCBot.MCBot()

def init(file):
    properties = bot_properties.MoonCommandBotProperties()
    config = json_helper.load_json(file)
    properties.trello_ky = config.trello_key
    properties.discord_tk = config.discord_token
    properties.bot_color = config.bot_color
    properties.bot_prefix = config.bot_prefix
    properties.join_message = config.join_message
    properties.current_game = config.playing

init("config.json")

globals.properties.discord_bot.run(globals.properties.discord_tk)
