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
    context.response = context.session.post(url=url, json=data)

    try:
        context.player.append(context.response.json())
    except ValueError as error:
        raise error

#############################
# Get Requests
##############

@when('I get the list of all players')
def step_impl(context):

    url = helper.build_url(context.base_address, "players")
    context.response = context.session.get(url=url)

@when('I get a player by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    context.response = context.session.get(url=url)

@when(u'I get a player by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player")
    data = {}
    for row in context.table:
        data.append(row["key"], row["field"])
    context.response = context.session.get(url=url, json=data)

@when(u'I get the list of the player leaderboard')
def step_impl(context):

    url = helper.build_url(context.base_address, "players", "leaderboard")
    context.response = context.session.get(url=url)


#############################
# Put Requests
##############

@when(u'I update a players details by id')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    context.response = context.session.put(url=url)

@when(u'I update a players details by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    data = {}
    for row in context.table:
        data.append(row["key"], row["field"])
    context.response = context.session.put(url=url, json=data)

@when(u'I update a match')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    data = {"winner": {}, "loser": {}}
    for row in context.table:
        data[row["player"]].append(row["key"], row["field"])
    context.response = context.session.put(url=url, json=data)

#############################
# Delete Requests
##############

@when(u'I remove a player')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    context.response = context.session.delete(url=url)

@when(u'I remove a player by body')
def step_impl(context):

    url = helper.build_url(context.base_address, "player", context.playerid)
    data = {}
    for row in context.table:
        data.append(row["key"], row["field"])
    context.response = context.session.delete(url=url, json=data)
