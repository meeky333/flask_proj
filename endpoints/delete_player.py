from player import Player
import assistance as assist

from flask import Flask, request, jsonify
from flask_api import status
import werkzeug

def decipher_delete_type(playerid):

    try:
        body = request.get_json(force=True)
        return delete_player_with_body(body)

    except werkzeug.exceptions.BadRequest:
        return delete_player_with_id(playerid)

    except Exception as error:
        return error, status.HTTP_400_BAD_REQUEST

def delete_player_with_id(playerid):
    """process run if the request method is DELETE"""

    players_list = assist.deserialize_players()

    for player in players_list:
        if player.playerid == playerid:

            players_list.remove(player)

            assist.serialize_players(players_list)
            return "OK", status.HTTP_200_OK

    return "Player ID does not exist", status.HTTP_400_BAD_REQUEST

def delete_player_with_body(identifiers):

    players_list = assist.deserialize_players()
    match_index = list()

    for index, player in enumerate(players_list):
        for indentifier_index, (key, value) in enumerate(identifiers.iteritems()):

            if not player.get_player()[key] == value: break
            if indentifier_index == len(identifiers)-1:
                match_index.append(index)

    if len(match_index) == 1:

        match_index = match_index[0]

        players_list.pop(match_index)
        assist.serialize_players(players_list)

        return "OK", status.HTTP_200_OK

    if len(match_index) > 1:
        return "results containt more than one player", status.HTTP_400_BAD_REQUEST
    else:
        return "No results were found", status.HTTP_400_BAD_REQUEST
