# Author: Johan Tan
import sys
try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
from utils import permissions, discord_helpers, default
class MCBot:
    def __init__(self, bot):
        config = default.get("config.json")
        self.bot = bot
        self.trello_client = ''
        self.discord_tk = config.discord_token
        self.trello_ky = config.trello_key
        self.trello_tk = ''
        self.bot_color = config.bot_color
        self.channel = ''
        self.join_message = config.join_message
        self.current_game = config.playing
    @commands.command(name="assign",
                    description="Assigns bot to the current channel the command is on.",
                    pass_context = True)
    async def assign(ctx):
        self.channel = ctx.message.channel
        await discord_helpers.send_message(self.bot,"Assigned to " + str(ctx.message.channel.name))

    @commands.command(name="pingtrello",
                    description='Tests bot connectivity to Trello')
    async def ping_trello(self):
        if(check_trello()):
            start = time.time()
            boards = self.trello_client.list_boards()
            end = time.time()
            embed = discord.Embed(title="Pong!", description="Time elapsed {time:3f} seconds".format(time=(end-start)), color=self.bot_color)
            await send_embed(embed)
        else:
            embed = discord.Embed(title="Error!", description="Trello client not connected. Please use MC!token and MC!link to connect the trello to the bot.", color=self.bot_color)
            await discord_helpers.send_embed(self,embed)
    @commands.command(name="token",
                    description="Supplies the user a link to determine the token that the bot will use.")
    async def token(self):
        await message("https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Moon%20CommandBot&key="+self.trello_ky)
    @commands.command(name="link",
                    description="Links the bot to the trello account with the correct token")
    async def link(self,api_token):
        self.trello_tk = api_token
        self.trello_client = TrelloClient(
            api_key=self.trello_ky,
            token=self.trello_tk
        )
        await message("Received token of Token: " + self.trello_tk)
    def check_trello():
        if(self.trello_client == ""):
            return False
        else:
            return True
def setup(bot):
    bot.add_cog(MCBot(bot))
