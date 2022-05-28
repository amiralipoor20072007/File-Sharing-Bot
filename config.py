import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = "5356530352:AAFFNNHhYh0VWubQarZ0aSsbYMX_OFLNhHI"

#Your API ID from my.telegram.org
APP_ID = 9981563

#Your API Hash from my.telegram.org
API_HASH = "7d259a24c15b4fea5151b1994dfcf7b0"

#Your db channel Id
CHANNEL_ID = -1001572029549

#OWNER ID
OWNER_ID = 2075613301

#Database 
DB_URI = "postgres://sgnbheul:RScgWWRS9BN2_uZ0e2U5BKnlUJxXDQb8@tyke.db.elephantsql.com/sgnbheul"

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = 0

TG_BOT_WORKERS = 4

#start message
START_MSG = "سلام {mention} آیدی شما : {id} \n\nبهترین آپلودرفایل تلگرام : @MahdiXiFS_Bot\n\nبا معرفی ما به دوستانتان از ما حمایت کنید."
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>"

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = "{filename}\n{previouscaption}\n\nاز آپلودرفایل ما حمایت کنید\n@MahdiXiFS_Bot"

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
