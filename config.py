from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "13382500"))
API_HASH = getenv("API_HASH", "6f5691b23c6f032eaae722e96d7e2459")

BOT_TOKEN = getenv("BOT_TOKEN", "5873474775:AAF87-0BXKcp0VcIpg0hKm-0QF0zWIqdlwE")
OWNER_ID = int(getenv("OWNER_ID", "6102257906"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://monivps6:monivps6@cluster0.n9ytmzd.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "https://t.me/TMK_MUSICCHANNEL")
