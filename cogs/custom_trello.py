try:
    from discord.ext import commands
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)
import

class CustomTrello:
    def __init__(self, client, trello_client):
        self.client = client
        self.trello_client = trello_client
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
        global API_TK
        API_TK = api_token
        global trello_client
        trello_client = TrelloClient(
            api_key=API_KY,
            token=API_TK
        )
        await message("Received token of Token: " + API_TK)


def setup(client):
    client.add_cog(CustomTrello(client))
