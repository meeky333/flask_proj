from player import Player
import assistance as assist

from flask import Flask, request, jsonify
from flask_api import status
import werkzeug

def decipher_post_type():
    return request_type_post()

def request_type_post():
    """process run if the request method is POST"""

    players_list = assist.deserialize_players()
    print("Players_list: {}".format(players_list))

    content = request.get_json()
    player = Player(
        firstname=content["firstname"],
        lastname=content["lastname"],
        wins=content["wins"],
        losses=content["losses"])

    print("Created player: {}".format(player.get_player()))

    players_list.append(player)

    assist.serialize_players(players_list)

    return player.get_player(), status.HTTP_201_CREATED
