from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = int(getenv("API_ID", "19197570"))
API_HASH = getenv("API_HASH", "0401e837796d193ec9ae6e17cb8cfbf8")

BOT_TOKEN = getenv("BOT_TOKEN", "7871663304:AAEIbappsY5FRC-44--dh5Fdkcd6zN1spXw")
OWNER_ID = int(getenv("OWNER_ID", "5444362033"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mukeshmonidb:mukeshmoni@cluster0.e27s9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "TMK_MUSICCHANNEL")
