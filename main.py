# built-in
import argparse
import logging
from itertools import cycle

# in-house
import assistance as assist
from endpoints import get_player, post_player, put_player, delete_player

# third-party
from flask import Flask, request, jsonify
from flask_api import status
import werkzeug


parser = argparse.ArgumentParser()
parser.add_argument('--host', default="localhost", help="select host")
parser.add_argument('--port', default="5000", help="select port")
parser.add_argument('--logging_level', default="info", help="set logging level")

args = parser.parse_args()

app = Flask("__name__")

try:
    exec("level = logging.{}".format(args.logging_level.upper()))
except Exception:
    print("could not assign logging level. Defaulting to INFO")
    level = logging.INFO

logging.basicConfig(level=level)

players_list = assist.deserialize_players()

#######################################
# Routes
###################


@app.route('/player', methods=["POST", "GET", "PUT", "DELETE"])
@app.route('/player/<playerid>', methods=["GET", "PUT", "DELETE"])
def player(playerid=None):
    """Parses the request type and sends the request to the correct method accordingly"""

    if request.method == 'POST':
        resp, code = post_player.decipher_post_type()
    elif request.method == 'GET':
       resp, code = get_player.decipher_get_type(playerid=playerid)
    elif request.method == 'PUT':
        resp, code = put_player.decipher_put_type(playerid=playerid)
    elif request.method == 'DELETE':
        resp, code = delete_player.decipher_delete_type(playerid=playerid)

    return jsonify(resp), code


@app.route('/players')
def players():
    """Returns a list of all players"""

    players_details = [player.get_player() for player in assist.deserialize_players()]
    return jsonify(players_details)


@app.route('/players/leaderboard', methods=["GET"])
def leaderboard():
    """Returns a list of all players in order of win/loss ratio unless specified otherwise"""

    reverse = True
    orderby = "ratio"

    players = assist.deserialize_players()
    try:
        content = request.get_json()
    except werkzeug.exceptions.BadRequest:
        pass
    else:
        if 'reverse' in content.keys() and isinstance(content['reverse'], bool):
            reverse = content['reverse']
        if 'orderby' in content.keys() and isinstance(content['orderby'], unicode):
            orderby = content['orderby']

    ways_to_order = [
        ["ratio", "wins", "firstname"],
        ["wins", "ratio", "firstname"],
        ["losses", "ratio", "firstname"],
        ["firstname", "lastname", "ratio"],
        ["lastname", "firstname", "ratio"]
    ]

    for order in ways_to_order:
        if orderby == order[0]:

            sorted_players = sorted(
                players, key=lambda player: [(getattr(player, attribute)) for attribute in order], reverse=reverse)
            return jsonify([player.get_player() for player in sorted_players])

    return "Cannot order", status.HTTP_400_BAD_REQUEST


@app.route('/match', methods=['PUT'])
def match():
    """Perform a match between 2 players"""

    players_list = assist.deserialize_players()
    match_index = list()

#######################################
# Check for request errors
###################

    try:
        body = request.get_json()
    except werkzeug.exceptions.BadRequest as error:
        return "Request must contain a body: {}".format(error), status.HTTP_400_BAD_REQUEST

    for parameter in ["winner", "loser"]:
        if not parameter in body:
            return "{} is not in the request body".format(parameter), status.HTTP_400_BAD_REQUEST

    try:
        player_guide = players_list[0].get_player()
    except:
        return "There are no players", status.HTTP_405_METHOD_NOT_ALLOWED

    winner = body["winner"]
    loser = body["loser"]

    for (index, parameter) in enumerate(winner):
        if not parameter in player_guide:
            return "{} is not a valid parameter".format(parameter), status.HTTP_400_BAD_REQUEST
        elif not type(winner[parameter]) == type(player_guide[parameter]):
            return "{} is not the correct datatype, it should be: {}".format(type(winner[parameter]), type(player_guide[parameter]))

#######################################
# Identify the winner and the loser
###################

    for index, player in enumerate(players_list):

        # looking for winner
        for identifier_index, (key, value) in enumerate(winner.iteritems()):
            if not player.get_player()[key] == value: break
            if identifier_index == len(winner)-1:
                player.wins += 1
                player.recalculate_ratio()

        # looking for loser
        for identifier_index, (key, value) in enumerate(loser.iteritems()):
            if not player.get_player()[key] == value: break
            if identifier_index == len(loser)-1:
                player.losses += 1
                player.recalculate_ratio()

    assist.serialize_players(players_list)

    return "ACCEPTED", status.HTTP_202_ACCEPTED

if __name__ == '__main__':
    app.run(debug=True, host=args.host, port=args.port)
