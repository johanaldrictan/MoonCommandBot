import requests
import aiohttp
import asyncio
import json
from discord.ext.commands import Bot
from discord import Game

BOT_PREFIX = "MC!"

TOKEN = 'NDk3NTQ5ODAxMjQ0NzIxMTYy.DphC3Q.VwFKLNF4P4Bb7frTT6Yqug8z6P4'
API_TK = '';
API_KY = '';

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Human Commander'))
    print("Logged in as " + client.user.name)

#@client.command(name='test',
#                description='Test function',
#                brief='Testing',
#                alias=['testing', 'test2'])

@client.command(name='authorizelink',
                description='Provides authorization link for the bot to receive a token.' +
                'Please ensure that this command is called first.',
                brief='Provides link for a token for the bot.',
                alias=['authlink', 'link'])
async def authorize_link():
    await client.say("https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Moon%20CommandBot&key=9a1338936b6585f8c72e9ae13c177b24")

@client.command(name='authorize',
                description='Gives the application the passed in api token. Please copy the token into the command.',
                brief='Gives the bot a token',
                alias=['auth'])
async def authorize(api_token):
    #check if token is valid...
    API_TK = api_token
    API_KY = '9a1338936b6585f8c72e9ae13c177b24'
    await client.say("Received token of Token: " + API_TK)
@client.command(name="ping",
                description='Tests bot connectivity to the board')
async def ping():
    url = 'https://api.trello.com/1/members/me/boards?key='+API_KY+'&token='+API_TK
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        if(response != 'invalid token'):
            response = json.loads(response)
        await client.say(url)

@client.command(name="logout")
async def logout():
    await client.say("Logging out.")
    await client.logout()

client.run(TOKEN)
