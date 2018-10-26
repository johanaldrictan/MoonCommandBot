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
"""
================================================================================
DEFAULT FUNCTIONALITY
================================================================================
    These functions are functions that are default to the TrelloAPI
"""
    @commands.command()
    async def addlist(self, ctx):
        return
    @commands.command()
    async def cardattach(self, ctx):

    @commands.command()
    async def closecard(self, ctx):

    @commands.command()
    async def closelist(self, ctx):

    @commands.command()
    async def createcard(self, ctx):

    @commands.command()
    async def editdesc(self, ctx):

    @commands.command()
    async def movecard(self, ctx):

    @commands.command()
    async def opencard(self, ctx):

    @commands.command()
    async def openlist(self, ctx):

    @commands.command()
    async def removecard(self, ctx):

    @commands.command()
    async def renamecard(self, ctx):

    @commands.command()
    async def renamelist(self, ctx):

    @commmands.command()
    async def addwebhook(self, ctx):

    @commands.command()
    async def editwebhook(self, ctx):

    @commands.command()
    async def removewebhook(self, ctx):

    @commands.command()
    async def webhooks(self, ctx):

    @commands.command()
    async def boardinfo(self, ctx):

    @commands.command()
    async def boards(self, ctx):

    @commands.command()
    async def card(self, ctx):

    @commands.command()
    async def lists(self, ctx):

    @commands.command()
    async def switch(self, ctx):

    @commands.command()
    async def viewlist(self, ctx):

    @commands.command()
    async def invitetoboard(self, ctx):

    @commands.command()
    async def removefromboard(self, ctx):

    @commands.command()
    async def attach(self, ctx):
        self.NotImplemented(ctx)

"""
================================================================================
CUSTOM FUNCTIONALITY
================================================================================
    These are bot functionalities that are custom to MCBot itself
"""
    async def daily_reminder_task():
        """ This function individually messages all the users ho have registered
            their trello account to the bot"""
    async def on_ready(self):
        """ Event to initialize bot tasks and other bot functions"""
        self.loop.create_task(reminder_task)

"""
================================================================================
HELPER FUNCTIONS
================================================================================
"""
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
    def NotImplemented(self, ctx):
        await self.send_message(ctx, "Function not implemented yet")
def setup(bot):
    bot.add_cog(MCBot(bot))
