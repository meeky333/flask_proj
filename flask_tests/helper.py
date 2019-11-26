import random
import names


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
        "firstname": names.get_first_name(),
        "lastname": names.get_last_name(),
        "wins": random.randint(0, 10),
        "losses": random.randint(0, 10)
    }