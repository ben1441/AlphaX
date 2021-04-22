import os 
from telethon.tl.types import ChatBannedRights 
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class config(object):
       LOGGER = True 
       # GET YOUR own value from my.telegram.org mere kang maat karna "-" 
       SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\.") 
       TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Modified") 
       BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        DATABASE_URI = os.environ.get("DATABASE_URI", None) 
        SESSION_STRING = os.environ.get("SESSION_STRING", None)
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", None))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want ULTRA's features
        UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None,
            view_messages=None,
            send_messages=True
        )
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs 
        CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None) 
        ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
        ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
        #SUPERFEDBAN
        FBAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None)
        if FBAN_GROUP_ID:
            FBAN_GROUP_ID = int(FBAN_GROUP_ID)
        EXCLUDE_FED = os.environ.get("EXCLUDE_FED", None)
        FBAN_GROUP = int(os.environ.get("FBAN_GROUP", False))
else:
    class Config(object):
        DB_URI = None