import os


class Config(object):
    TG_BOT_TOKEN = "5267257900:AAEabm-lQdTAAfYhaw3KvKTB4lcJhQ8UGcw"
    APP_ID = 13519785
    API_HASH = "22a8c34e40082b2fce539266efa1f531"
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5122474448").split())
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", None)
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S", ""
    ) # https://placehold.it/90x90
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = ""
    DATABASE_NAME = "LegendBot"
    DATABASE_URL = "mongodb+srv://LegendBoy:Krishna_@01_@01@cluster0.pahsr.mongodb.net/?retryWrites=true&w=majority"
