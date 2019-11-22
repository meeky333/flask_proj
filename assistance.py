import os
import json
import logging

from player import Player

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "{}/player.json".format(dir_path)

def deserialize_players():

    players = []
    with open(filename, "r") as f:
        try:
            players_list = json.load(f)
        except Exception:
            print("could not load file")
            players_list = []

        for json_player in players_list:

            player = Player(
                firstname=json_player["firstname"],
                lastname=json_player["lastname"],
                wins=json_player["wins"],
                losses=json_player["losses"])

            if "playerid" in json_player:
                player.playerid = json_player["playerid"]

            players.append(player)

        return players

def serialize_players(players_list):

    players_list = [player.get_player() for player in players_list]

    with open(filename, "w") as f:
        json.dump(players_list, f)

def check_for_keys(content, expected_keys):
    keys = []
    for key in expected_keys:
        if key not in content:
            keys.append(key)
    return keys

if __name__ == "__main__":
    deserialize_players()