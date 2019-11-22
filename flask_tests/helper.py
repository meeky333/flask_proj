import random
import namegenerator


def build_url(*args):
    return "/".join(args)


def get_type_from_string(type_string):
    types = {"dictionary": dict,
             "string": str,
             "unicode": unicode,
             "integer": int,
             "bool": bool,
             "list": list}
    return types.get(type_string)

def new_player():
    """Creates a new player with random name and wins/losses
    and returns the player as a dictionary"""

    return {
        "firstname": namegenerator.gen(),
        "lastname": namegenerator.gen(),
        "wins": random.randint(0, 100),
        "losses": random.randint(0, 100)
    } 