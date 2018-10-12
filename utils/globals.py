import bot_properties
import json_helper

#file is the config.json file
def init(file):
    global properties
    properties = MoonCommandBotProperties()
    config = json_helper.load_json(file)
    properties.trello_ky = config.trello_key
    properties.discord_tk = config.discord_token
    properties.bot_color = config.bot_color
    properties.bot_prefix = config.bot_prefix
    properties.join_message = config.join_message
    properties.current_game = config.playing
