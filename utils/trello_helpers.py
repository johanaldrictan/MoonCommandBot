from utils import globals

global properties

def check_trello():
    if(globals.properties.trello_client == ""):
        return False
    else:
        return True
