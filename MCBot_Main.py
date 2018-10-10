#  MCBot_Main.py
#  main entry point for the Moon CommandBot
#  Author: Johan Tan
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


extensions = ['']

client = Bot(command_prefix=BOT_PREFIX)
trello_client = ""

@client.event
async def on_ready():
    await client.change_presence(game=Game(name=''))
    print("Logged in as " + client.user.name)


def check_trello():
    global trello_client
    if(trello_client == ""):
        return False
    else:
        return True

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded [{}]'.format(extension,error))
@client.command()
async def load(extension):
    try:
        client.unload_extension(extension)
        print('unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded [{}]'.format(extension,error))

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension,error))

client.run(DISCORD_TK)
