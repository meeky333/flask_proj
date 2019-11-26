import json

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

#############################
# Get Requests
##############

@when('I get the list of all players')
def step_impl(context):

    url = helper.build_url(context.base_address, "players")

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)

    context.logger.info(context.response)

@when('I get a player by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)

    context.logger.info(context.response)

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

    context.logger.info(context.response)

@when(u'I get the list of the player leaderboard')
def step_impl(context):

    url = helper.build_url(context.base_address, "players", "leaderboard")

    with context.vcr.use_cassette("get_requests.json"):
        context.response = context.session.get(url=url)

    context.logger.info(context.response)


#############################
# Put Requests
##############

@when(u'I update a players details by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.player["playerid"])
    data = {
        changes = helper.new_player()
    }


    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.put(url=url)

    context.logger.info(context.response)

@when(u'I update a players details by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    data = {
        "firstname": context.player["firstname"],
        "lastname": context.player["lastname"],
        "wins": context.player["wins"],
        "losses": context.player["losses"]
    }

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.put(url=url, json=data)

    context.logger.info(context.response)

@when(u'I update a match')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    data = {"winner": {}, "loser": {}}
    for row in context.table:
        data[row["player"]].append(row["key"], row["field"])

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.put(url=url, json=data)

    context.logger.info(context.response)

#############################
# Delete Requests
##############

@when(u'I remove a player')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)

    with context.vcr.use_cassette("delete_requests.json"):
        context.response = context.session.delete(url=url)

    context.logger.info(context.response)

@when(u'I remove a player by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    data = {}
    for row in context.table:
        data.append(row["key"], row["field"])

    with context.vcr.use_cassette("put_requests.json"):
        context.response = context.session.delete(url=url, json=data)

    context.logger.info(context.response)
