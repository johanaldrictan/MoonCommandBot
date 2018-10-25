import time
import aiohttp
import discord
import asyncio

from asyncio.subprocess import PIPE
from discord.ext import commands
from io import BytesIO
from utils import repo, default, http, dataIO


class Admin:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self._last_result = None

    @commands.command()
    @commands.check(repo.is_owner)
    async def reload(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"cogs.{name}")
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```\n{e}```")
        await ctx.send(f"Reloaded extension **{name}.py**")

    @commands.command()
    @commands.check(repo.is_owner)
    async def logout(self, ctx):
        """ Reboot the bot """
        await ctx.send('Rebooting now...')
        time.sleep(1)
        await self.bot.logout()

    @commands.command()
    @commands.check(repo.is_owner)
    async def load(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```diff\n- {e}```")
        await ctx.send(f"Loaded extension **{name}.py**")

    @commands.command()
    @commands.check(repo.is_owner)
    async def unload(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(f"```diff\n- {e}```")
        await ctx.send(f"Unloaded extension **{name}.py**")

    @commands.group()
    @commands.check(repo.is_owner)
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            _help = await ctx.bot.formatter.format_help_for(ctx, ctx.command)

            for page in _help:
                await ctx.send(page)

    @change.command(name="playing")
    @commands.check(repo.is_owner)
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

    @change.command(name="username")
    @commands.check(repo.is_owner)
    async def change_username(self, ctx, *, name: str):
        """ Change username. """
        try:
            await self.bot.user.edit(username=name)
            await ctx.send(f"Successfully changed username to **{name}**")
        except discord.HTTPException as err:
            await ctx.send(err)

def setup(bot):
    bot.add_cog(Admin(bot))
