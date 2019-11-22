# Built in
import os
import logging

# Third party
import requests
from behave import use_fixture


def before_all(context):
    context.tlog = logging.getLogger("FlaskTests")
    context.base_address = os.getenv("MBASE_ADDR", "http://127.0.0.1:5000")
    context.player = []

    context.session = requests.Session()

    # logging.getLogger("urllib3").setLevel(logging.WARNING)
