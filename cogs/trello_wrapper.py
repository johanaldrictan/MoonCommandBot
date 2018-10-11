try:
    from discord.ext import commands
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)

class TrelloWrapper:
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self):
        await self.client.say('Pong!')
