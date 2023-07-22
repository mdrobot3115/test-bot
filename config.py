#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5162572062:AAEvGeB0qoU7y7E7Jei6Ow6Pw4Eq7RsunKs")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "9844066"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCWNWIAXhS9evBqieLQuxBM0AEP8Ajw2xDIoWL_L_By2bvgzZJABw_IhfHi5PfpRn2J_gtHHP-zgD_8IiVHq8-rCDzS12usRcOY8EUvl1S7xdKqM66jaTchO4RTmgI2jdWqbx51UxI_11-GX_i-QL_GT7pxG7x7eLvC-Y8WU2xH_W2tSp06b_muV0zaDfee6B2KcLLakix0q0h4BHfT6z-nqBmY9SCierEpIq3mUsVXphOR927BrU-6DaPUyHxOGCu07e9J9g5zFEyBdWN8xmgmtPpBemIfxCUvrvVjoqt6siVTdW6eBGSeqvP7k8tmUYM-EX4KmByyJGfTudkHEQSeb4ihZAAAAABphwJ4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://web_mlt_user:JW72gfH0EqaS2TwUoW0c6w0Ppyzq8FBy@dpg-chkfq4m7avj217e0kcjg-a.oregon-postgres.render.com/web_mlt")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
