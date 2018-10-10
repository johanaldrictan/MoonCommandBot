try:
    from discord.ext import commands
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)

class BasicBot:
    def __init__(self, client):
        self.client = client

    @commands.command(name="hello",
                    description='Hello')
    async def hello(self):
        await self.client.say("Pong!")

    @commands.command(name="assign",
                    description="Assigns bot to the current channel the command is on.",
                    pass_context = True)
    async def assign(ctx):
        global channel
        channel = ctx.message.channel
        await send_message(self.client,"Assigned to " + str(ctx.message.channel.name))

    @commands.command(name="logout")
    async def logout(self):
        await message("Logging out.")
        print("Logging out.")
        await self.client.logout()
