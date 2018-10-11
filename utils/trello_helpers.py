import globals

def check_trello():
    global properties.trello_client
    if(properties.trello_client == ""):
        return False
    else:
        return True
