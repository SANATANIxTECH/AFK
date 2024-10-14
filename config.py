from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", "28795512"))
API_HASH = getenv("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")

BOT_TOKEN = getenv("BOT_TOKEN", "7476540645:AAHjMhqy2vf6KBB-BBoZWZMRIjYoo2EPyCA")
LOG_ID = int(getenv("LOG_ID", "-1002090474484"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sanatanixtech:sachin@sachin.9guym.mongodb.net/?retryWrites=true&w=majority&appName=Sachin")
SUDO_USER = list(map(int, getenv("SUDO_USER", "7373125778").split()))
