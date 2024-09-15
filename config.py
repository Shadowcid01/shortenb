#(©)Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7320367980:AAGivLmaX2j9NEWUupC3XbudtI_F-4waUVA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28909229"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a85d6a95d4e6cff3b02fefd3d27575c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002079159862"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6204450961"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://PfmBots:PfmBots@cluster0.yvumulz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "0"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Set to `False` to disable auto link creation, or `True` to enable Auto link creation.
ENABLE_LINK_CREATION = True 

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ {first}\n <blockquote>ɪ'ᴍ ᴘꜰᴍ ꜰɪʟᴇꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴍᴇ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴀᴛ @AudioVerseNetwork.</blockquote>")
try:
    ADMINS=[6204450961]
    for x in (os.environ.get("ADMINS", "891528999").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐁𝐫𝐨/𝐒𝐢𝐬 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", '{previouscaption}\n <code>{filename}</code> <blockquote><b>» ʙʏ @AudioVerseNetwork</b></blockquote>')

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "True") == "True"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n<blockquote>» ᴍʏ ᴏᴡɴᴇʀ : @AudioVerseNetwork</blockquote>"

ADMINS.append(OWNER_ID)
ADMINS.append(6204450961)

LOG_FILE_NAME = "filesharingbot.txt"


# Ensure these are set correctly in config.py
SHORTENER_API = os.environ.get("SHORTENER_API", "0aef028290a85e9346edab753a4d557a7458d6e4")
SHORTENER_WEBSITE = os.environ.get("SHORTENER_WEBSITE", "https://urlshortx.io")
SHORTENER_API2 = os.environ.get("SHORTENER_API2", "d86f57a6ae444bdc63318e7b111a02b8edb8a59a")
SHORTENER_WEBSITE2 = os.environ.get("SHORTENER_WEBSITE2", "https://linkshortx.in")

# LinkShortner Added
LINKSHORTX_API= os.environ.get("LINKSHORTX_API",'5b2908ac9710e83f0a4186a74c25ca3e728faac6')
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
