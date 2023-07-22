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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQDQj9UAmWz61GiK1UmTFhVmPk8BjXdxhszvItqU2q7ShzZlJA_HGu-bsREVx-6pVyBM7OYOJxWpjgUrznpmesdE_ODnwqN8AzyTInd-NS3YN5ViPcCeiwVYafVCNZ3Qrzn1si7OPjUO404_Gj0tjhgqbHs_ouiBinNjaRR-4agDOczAU9jaJGnWBKBIJ4WsJvGmJcYd0dKp67LvTlFDlkxbPeSVuQHQ7Csz48e3sJtK5b-HedXnpTX9-gL9Is1v2TCa04dZ3gX6PzJ9STf3mOI1aOQH0-O4Ney5PeG_mwNJzRDrjUrn-AW0ifi8cJf0dSMiGpkFtMseCO5p-SjjX3ebSWoZ9wAAAABphwJ4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://web_mlt_user:JW72gfH0EqaS2TwUoW0c6w0Ppyzq8FBy@dpg-chkfq4m7avj217e0kcjg-a.oregon-postgres.render.com/web_mlt")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
