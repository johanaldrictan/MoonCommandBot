# helper.py
# contains helper functions
# Author: Johan Tan
#------------------------------------------------------------------------------
import json

from collections import namedtuple
def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())
def json2obj(data):
    return json.load(data, object_hook=_json_object_hook)
def load_json(file):
    try:
        with open(file, encoding='utf8') as data:
            return json2obj(data)
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")
