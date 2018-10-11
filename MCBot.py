try:
    from utils import permissions
    from discord.ext.commands import AutoShardedBot
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)

class MCBot(AutoShardedBot):
    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot or not permissions.can_send(msg):
            return

        await self.process_commands(msg)
