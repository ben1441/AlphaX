import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ALPHAX import ALIVE_NAME, StartTime
from ALPHAX.utils import admin_cmd
from ALPHAX import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from ALPHAX.helpers.functions import get_readable_time
import time
import os
import datetime
# importing ENDED HERE
from ALPHAX import botname
BOT = str(botname) if botname else "Aℓρђα ㄨ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Aℓρђα ㄨ user"
tim = get_readable_time((time.time() - StartTime))
# ALIVE_PIC
PIC = os.environ.get("ALIVE_PIC")
#up-time
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
# bot
ALPHAX = "[ALPHAX](https://t.me/AlphaXUpdates)"
#repo 
ALPHAX = "[ALPHAX](https://github.com/Thealphax/Alphax"
#support NAME = "[{MASTER}](tg://user?id={A})"
global warns
A = bot.uid
MASTER = f"[{NAME}](tg://user?id={A})"
GROUP = "[SUPPORT GROUP](https://t.me/Alphaxhelpchat)
ALIVE = "Your AlphaX IS ON😊" 
ALPHA = "MY MASTER IS USING AlphaX USERBOT"
EMOJI = "😊"
