try:
    from discord.ext.commands import Bot
except ImportError:
    print("Discord.py is not installed.\n")
    sys.exit(1)

#DISCORD MESSAGE HELPERS
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
