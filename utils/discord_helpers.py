import discord

async def send_message(client,message):
    #if channel is unassigned, use the regular channel
    if(channel == ""):
        await client.say(message)
    else:
        await client.send_message(channel,message)
async def send_embed(client,embed):
    #if channel is unassigned, use the regular channel
    if(channel == ""):
        await client.say(embed=embed)
    else:
        await client.send_message(channel,embed=embed)
