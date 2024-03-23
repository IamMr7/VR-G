import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 27665416))

    API_HASH = os.environ.get("API_HASH", "08c3c88fabc72ea8554ffc74845b2185")
