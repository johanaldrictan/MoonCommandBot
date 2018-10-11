# admin.py
# file that contains commands for administration of the server or the bot
# Thanks AlexFlipnote for posting a template for creating a discord bot using cogs!
#------------------------------------------------------------------------------
import time
import aiohttp
import discord
import asyncio

from asyncio.subprocess import PIPE
from discord.ext import commands
from io import BytesIO
from utils import permissions, bot_properties


class Admin:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self._last_result = None

    @commands.command(name="hello",
                    description='Hello')
    async def hello(self):
        await self.client.say("Pong!")

    @commands.command(name="assign",
                    description="Assigns bot to the current channel the command is on.",
                    pass_context = True)
    async def assign(ctx):
        global properties
        properties.channel = ctx.message.channel
        await send_message(self.client,"Assigned to " + str(ctx.message.channel.name))

    @commands.command(name="logout")
    async def logout(self):
        await message("Logging out.")
        print("Logging out.")
        await self.client.logout()

    @commands.command()
    @commands.check(permissions.is_administrator)
    async def reload(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"cogs.{name}")
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```\n{e}```")
        await ctx.send(f"Reloaded extension **{name}.py**")

    @commands.command()
    @commands.check(permissions.is_administrator)
    async def reboot(self, ctx):
        """ Reboot the bot """
        await ctx.send('Rebooting now...')
        time.sleep(1)
        await self.bot.logout()

    @commands.command()
    @commands.check(permissions.is_administrator)
    async def load(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```diff\n- {e}```")
        await ctx.send(f"Loaded extension **{name}.py**")

    @commands.command()
    @commands.check(permissions.is_administrator)
    async def unload(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```diff\n- {e}```")
        await ctx.send(f"Unloaded extension **{name}.py**")

    @change.command(name="playing")
    @commands.check(permissions.is_administrator)
    async def change_playing(self, ctx, *, playing: str):
        """ Change playing status. """
        try:
            await self.bot.change_presence(
                activity=discord.Game(type=0, name=playing),
                status=discord.Status.online
            )
            dataIO.change_value("config.json", "playing", playing)
            await ctx.send(f"Successfully changed playing status to **{playing}**")
        except discord.InvalidArgument as err:
            await ctx.send(err)
        except Exception as e:
            await ctx.send(e)

    @change.command(name="nickname")
    @commands.check(permissions.is_administrator)
    async def change_nickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"Successfully changed nickname to **{name}**")
            else:
                await ctx.send("Successfully removed nickname")
        except Exception as err:
            await ctx.send(err)


def setup(bot):
    bot.add_cog(Admin(bot))
