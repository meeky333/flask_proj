# Built in
import os
import shutil
import logging

# Third party
import requests
import vcr
from behave import use_fixture


def before_all(context):
    context.logger = logging.getLogger("FlaskTests")
    context.base_address = os.getenv("MBASE_ADDR", "http://127.0.0.1:5000")
    context.player = {}

    context.session = requests.Session()

    context.vcr = vcr.VCR(
        serializer="json",
        cassette_library_dir="cassettes",
        record_mode="new_episodes",
        match_on=["uri", "method"])

    logging.getLogger("vcr").setLevel(logging.WARNING)

def after_all(context):

    # Delete all cassettes after tests are finished
    shutil.rmtree("cassettes")

    # delete the players list after tests are finished
    # os.remove("../player.json")
