import os
from os import environ

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN = int(os.environ.get("ADMIN"))
START_IMG = os.environ.get("START_IMG")
START_MSG = os.environ.get("START_MSG")
BUTTON_1 = os.environ.get("BUTTON_1")
BUTTON_2 = os.environ.get("BUTTON_2")
LINK_1 = os.environ.get("LINK_1")
LINK_2 = os.environ.get("LINK_2")
