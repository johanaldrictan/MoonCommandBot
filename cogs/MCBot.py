# Author: Johan Tan
import sys
import time
try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
try:
    from trello import TrelloClient
except ImportError:
    print("Py-trello is not installed.\n")
from utils import permissions, default
class MCBot:
    def __init__(self, bot):
        config = default.get("config.json")
        self.bot = bot
        self.trello_client = ''
        self.discord_tk = config.discord_token
        self.trello_ky = config.trello_key
        self.trello_tk = ''
        self.bot_color = 0xf0efc8
        self.channel = ''
        self.join_message = config.join_message
        self.current_game = config.playing

    @commands.command()
    async def assign(self,ctx):
        """Assigns bot to the current channel
        the command is on."""
        self.channel = ctx.message.channel
        await self.send_message(ctx, "Assigned to " + str(ctx.message.channel.name))

    @commands.command()
    async def pingtrello(self, ctx):
        """Checks bot's connectivity to Trello"""
        if(self.check_trello()):
            start = time.time()
            boards = self.trello_client.list_boards()
            end = time.time()
            embed = discord.Embed(title="Pong!", description="Time elapsed {time:3f} seconds".format(time=(end-start)), color=int(self.bot_color))
            await self.send_embed(ctx, embed)
        else:
            embed = discord.Embed(title="Error!", description="Trello client not connected. Please use MC!token and MC!link to connect the trello to the bot.", color=int(self.bot_color))
            await self.send_embed(ctx, embed)
    @commands.command()
    async def token(self, ctx):
        """Supplies the user a link to determine
        the token that the bot will use."""
        await self.send_message(ctx, "https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Moon%20CommandBot&key="+self.trello_ky)
    @commands.command()
    async def link(self, ctx, api_token):
        """Links the bot to the trello account
         with the correct token"""
        self.trello_tk = api_token
        self.trello_client = TrelloClient(
            api_key=self.trello_ky,
            token=self.trello_tk
        )
        await self.send_message(ctx, "Received token of Token: " + self.trello_tk)
    def check_trello(self):
        if(self.trello_client == ""):
            return False
        else:
            return True
    async def send_message(self, ctx, message):
        if(self.channel == ""):
            channel =  ctx.message.channel
            await channel.send(message)
        else:
            await self.channel.send(message)
    async def send_embed(self, ctx, embed):
        if(self.channel == ""):
            channel = ctx.message.channel
            await channel.send(embed=embed)
        else:
            await self.channel.send(embed=embed)
def setup(bot):
    bot.add_cog(MCBot(bot))
