import json
import os

import helper

from behave import *


#############################
# Post Requests
##############

@when('I post a player')
def step_impl(context):

    url = helper.build_url(context.base_address, "player")
    data = helper.new_player()

    with context.vcr.use_cassette("post_requests.json"):
        context.response = context.session.post(url=url, json=data)

    try:
        context.player = context.response.json()
    except Exception:
        raise

@when('I post another player')
def step_impl(context):

    url = helper.build_url(context.base_address, "player")
    data = helper.new_player()

    with context.vcr.use_cassette("post_another_requests.json"):
        context.response = context.session.post(url=url, json=data)

    try:
        context.second_player = context.response.json()
    except Exception:
        raise

#############################
# Get Requests
##############

@when('I get the list of all players')
def step_impl(context):

    url = helper.build_url(context.base_address, "players")

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)


@when('I get a player by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)


@when(u'I get a player by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player")
    data = {
        "firstname": context.player["firstname"],
        "lastname": context.player["lastname"],
        "wins": context.player["wins"],
        "losses": context.player["losses"]
    }

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url, json=data)


@when(u'I get the list of the player leaderboard')
def step_impl(context):

    url = helper.build_url(context.base_address, "players", "leaderboard")

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)


@then(u'the winning player should have a win')
def step_impl(context):

    try:
        os.remove("cassettes/get_requests.json")
    except:
        pass

    url = helper.build_url(context.base_address, "player", context.player["playerid"])

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)

    result = context.response.json()[0]

    print(result)
    print(context.second_player)

    assert result["wins"] == context.player["wins"] + 1

@then(u'the losing player should have a loss')
def step_impl(context):

    try:
        os.remove("cassettes/get_another_request.json")
    except:
        pass

    url = helper.build_url(context.base_address, "player", context.second_player["playerid"])

    with context.vcr.use_cassette("get_another_request.json"):
        context.response = context.session.get(url=url)

    result = context.response.json()[0]

    print(result)
    print(context.second_player)

    assert result["losses"] == context.second_player["losses"]

#############################
# Put Requests
##############

@when(u'I update a players details by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])
    player_details = helper.new_player()
    data = {"changes": player_details}

    context.player = player_details

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.put(url=url, json=data)

    context.logger.info(context.response)

@when(u'I update a players details by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])
    player_details = helper.new_player()
    data = {
        "identification": {
            "firstname": context.player["firstname"],
            "lastname": context.player["lastname"],
            "wins": context.player["wins"],
            "losses": context.player["losses"]
        },
        "changes": player_details
    }

    context.player = player_details

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.put(url=url, json=data)

    context.logger.info(context.response)

@when(u'I update a match')
def step_impl(context):

    url = helper.build_url(context.base_address, "match")
    data = {
        "winner": context.player,
        "loser": context.second_player
    }

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.put(url=url, json=data)

    context.logger.info(context.response.content)

#############################
# Delete Requests
##############

@when(u'I remove a player by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])

    with context.vcr.use_cassette("delete_requests.json"):
        context.response = context.session.delete(url=url)

    context.logger.info(context.response)

@when(u'I remove a player by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])
    data = {}
    for row in context.table:
        data.append(row["key"], row["field"])

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.delete(url=url, json=data)

    context.logger.info(context.response)
