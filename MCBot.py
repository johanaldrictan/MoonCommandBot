import sys
try:
    from discord.ext.commands import Bot
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
from utils import permissions
class MCBot:
    def __init__(self):
        self.discord_client = ''
        self.trello_client = ''
        self.discord_tk = ''
        self.trello_ky = ''
        self.trello_tk = ''
        self.bot_color = ''
        self.bot_prefix = ''
        self.channel = ''
        self.join_message = ''
        self.current_game = ''
    @commands.command(name="assign",
                    description="Assigns bot to the current channel the command is on.",
                    pass_context = True)
    async def assign(ctx):
        global properties
        globals.properties.channel = ctx.message.channel
        await discord_helpers.send_message(self.bot,"Assigned to " + str(ctx.message.channel.name))

    @commands.command(name="logout")
    async def logout(self):
        await discord_helpers.send_message(self.bot,"Logging out.")
        print("Logging out.")
        await self.bot.logout()
    @commands.command(name="ping",
                    description='Tests bot connectivity to Trello')
    async def ping(self):
        if(check_trello()):
            start = time.time()
            boards = trello_client.list_boards()
            end = time.time()
            embed = discord.Embed(title="Pong!", description="Time elapsed {time:3f} seconds".format(time=(end-start)), color=color)
            await send_embed(embed)
        else:
            embed = discord.Embed(title="Error!", description="Trello client not connected. Please use MC!token and MC!link to connect the trello to the bot.", color=color)
            await send_embed(selfembed)
    @commands.command(name="token",
                    description="Supplies the user a link to determine the token that the bot will use.")
    async def token():
        await message("https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Moon%20CommandBot&key="+API_KY)
    @commands.command(name="link",
                    description="Links the bot to the trello account with the correct token")
    async def link(api_token):
        globals.proprties.trello_tk = api_token
        globals.properties.trello_client = TrelloClient(
            api_key=proprties.trello_ky,
            token=proprties.trello_tk
        )
        await message("Received token of Token: " + properties.trello_tk)
    
async def send_message(client,message):
    #if channel is unassigned, use the regular channel
    if(globals.properties.channel == ""):
        await client.say(message)
    else:
        await client.send_message(globals.properties.channel,message)
async def send_embed(client,embed):
    #if channel is unassigned, use the regular channel
    if(globals.properties.channel == ""):
        await client.say(embed=embed)
    else:
        await client.send_message(globals.properties.channel,embed=embed)
def check_trello():
    if(globals.properties.trello_client == ""):
        return False
    else:
        return True
