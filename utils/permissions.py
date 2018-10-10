# permissions.py
# wrapper functions for the implementation of permissions in Discord
# most functions were grabbed from the discord_bot.py project by AlexFlipnote
# Author: Johan Tan
#--------------------------------------------------------------------------
#import guard
try:
    from discord.ext import commands
    import discord
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)

def can_send(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).send_messages


def can_embed(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).embed_links


def can_upload(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).attach_files


def can_react(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).add_reactions


def is_nsfw(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.is_nsfw()

def is_administrator(ctx):
    return ctx.message.author.server_permissions.administrator
