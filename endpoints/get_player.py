import assistance as assist

from flask import Flask, request, jsonify
from flask_api import status
import werkzeug

def decipher_get_type(playerid):

    try:
        body = request.get_json(force=True)
        return get_player_with_body(body)

    except werkzeug.exceptions.BadRequest:
        return get_player_with_id(playerid)

    except Exception as error:
        return error, status.HTTP_400_BAD_REQUEST

def get_player_with_body(body):
    """process run if the request method contains a body"""

    players_list = assist.deserialize_players()

    if body is None:
        return "Request must have a body: {}".format(body), status.HTTP_400_BAD_REQUEST
    else:
        for item in body:
            print(players_list)
            players_list = filter(lambda player: player.get_player()[item] == body[item], players_list)

        return [player.get_player() for player in players_list], status.HTTP_200_OK

def get_player_with_id(playerid):
    """process run if the request method does not have a body"""

    players_list = assist.deserialize_players()

    if playerid is not None:

        result = list(filter(lambda player: player.get_player()["playerid"] == playerid, players_list))
        return [player.get_player() for player in result], status.HTTP_200_OK

    else:
        return "Requires a player ID or a body", status.HTTP_400_BAD_REQUEST


