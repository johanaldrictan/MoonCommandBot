# Author: Johan Tan
import sys
import time
import datetime
import json
import os
from pathlib import Path
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
from cogs import events
class MCBot:
    def __init__(self, bot):
        self.config = default.get("config.json")
        self.data = {}
        self.bot = bot
        self.trello_client = ''
        self.discord_tk = self.config.discord_token
        self.trello_ky = self.config.trello_key
        self.trello_tk = ''
        self.bot_color = 0xf0efc8
        self.channel = ''
        self.join_message = self.config.join_message
        self.current_game = self.config.playing
        self.last_reminded = datetime.datetime.now().date()

    @commands.command()
    async def assign(self,ctx):
        """Assigns bot to the current channel
        the command is on."""
        print(ctx.message.channel)
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
        if(self.trello_tk == ''):
            await self.send_message(ctx, "https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Moon%20CommandBot&key="+self.trello_ky)
        else:
            await self.send_message(ctx, "Bot is already connected to trello")
    @commands.command()
    async def link(self, ctx, api_token):
        """Links the bot to the trello account
         with the correct token"""
        if(self.trello_tk == ''):
            self.trello_tk = api_token
            self.trello_client = TrelloClient(
                api_key=self.trello_ky,
                token=self.trello_tk
            )
            if(self.data == {}):
                self.data['trello'] = []
                self.data['trello'].append({
                    'trello_tk': self.trello_tk
                })
            else:
                await self.send_message(ctx, "Trello already connected")
            await self.send_message(ctx, "Received token of Token: " + self.trello_tk)
        else:
            await self.send_message(ctx, "Token already received")
    #
    #===============================================================================
    #DEFAULT FUNCTIONALITY
    #===============================================================================
    #    These functions are functions that are default to the TrelloAPI
    #
    '''
    @commands.command()
    async def addlist(self, ctx):

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
    '''

    @commands.command()
    async def boards(self, ctx):
        if(self.check_trello()):
            boards = self.trello_client.list_boards()
            await self.send_message(ctx, boards)
        else:
            await self.send_message(ctx, "Trello not initialized get the token with `MC!token` and pass the given token into `MC!link`.")

    #
    #===============================================================================
    #CUSTOM FUNCTIONALITY
    #===============================================================================
    #    These are bot functionalities that are custom to MCBot itself
    #
    async def daily_reminder_task(self):
        """ This function individually messages all the users ho have registered
            their trello account to the bot """
        if(datetime.datetime.now().date() > self.last_reminded):
            self.last_reminded = datetime.datetime.now().date()
            print("reminded")

    async def on_ready(self):
        """ Event to initialize bot tasks and other bot functions"""
        self.bot.loop.create_task(self.daily_reminder_task())
        if(self.trello_tk == ''):
            #read
            file = Path("data.json")
            if(file.is_file()):
                 save = default.get("data.json")
                 if(getattr(save, 'trello', False)):
                     print("Reading token value from file: " + save.trello[0].trello_tk)
                     self.trello_tk = save.trello[0].trello_tk
                     self.trello_client = TrelloClient(
                         api_key=self.trello_ky,
                         token=self.trello_tk
                     )
    async def on_message(self, msg):
        if(msg.author == self.bot.user):
            return
        if(msg.content.startswith(self.config.prefix[0])):
            if(msg.content == "MC!logout"):
                try:
                    #self.data['channel'] = self.channel
                    with open("data.json", 'w', encoding = 'utf-8') as outfile:
                        json.dump(self.data, outfile)
                finally:
                    outfile.close()

    #
    #===============================================================================
    #HELPER FUNCTIONS
    #===============================================================================
    #
    def check_trello(self):
        if(self.trello_client == ""):
            return False
        else:
            return True
    def NotImplemented(self, ctx):
        self.send_message(ctx, "Function not implemented yet")
    async def send_message(self, ctx, message):
        if(self.channel == ""):
            channel =  ctx.message.channel
            await channel.send(message)
        else:
            await self.channel.send(message)
    async def send_message(self, msg, message):
        if(self.channel == ""):
            channel =  msg.channel
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
