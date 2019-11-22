import assistance as assist

from flask import Flask, request, jsonify
from flask_api import status
import werkzeug

def decipher_put_type(playerid):

    try:
        body = request.get_json(force=True)
    except Exception as error:
        return error, status.HTTP_400_BAD_REQUEST

    if "identification" in body:
        return put_player_with_body(body)
    else:
        return put_player_with_id(playerid)

def put_player_with_id(playerid):
    """process run if the request method is PUT"""

    original_list = assist.deserialize_players()
    players_list = original_list

    for index, _ in enumerate(players_list):
        if players_list[index].playerid == playerid:

            body = request.get_json()
            try:
                changes = body["changes"]
            except Exception as error:
                return error, status.HTTP_400_BAD_REQUEST

            for key, value in changes.items():
                if key in players_list[index].get_player():

                    if type(value) == type(players_list[index].get_player()[key]):
                        setattr(players_list[index], key, value)
                    else:
                        return "incorrect data type", status.HTTP_400_BAD_REQUEST

            assist.serialize_players(original_list)
            return "ACCEPTED", status.HTTP_202_ACCEPTED

    return "Player ID does not exist", status.HTTP_400_BAD_REQUEST

def put_player_with_body(body):

    original_list = assist.deserialize_players()
    players_list = original_list

    try:
        identification = body["identification"]
        changes = body["changes"]
    except Exception as error:
        return error, status.HTTP_400_BAD_REQUEST

    for item in identification:
        players_list = filter(lambda player: player.get_player()[item] == identification[item], players_list)
        if players_list == list():
            return "'{}' was not found amongst any players".format(item), status.HTTP_400_BAD_REQUEST

    if len(players_list) >= 2:
        return "results containt more than 1 player. \
        try to identify more specifically, or use the uuid", status.HTTP_400_BAD_REQUEST
    else:
        player = players_list[0]

        for key, value in changes.items():
            if key in player.get_player():

                if type(value) == type(player.get_player()[key]):

                    setattr(player, key, value)
                else:
                    return "incorrect data type", status.HTTP_400_BAD_REQUEST

        assist.serialize_players(original_list)
        return "ACCEPTED", status.HTTP_202_ACCEPTED