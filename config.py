import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COINMARKETCAP_API_KEY", "recuerda poner la api key en el .env")
API_URL_BASE = "https://pro-api.coinmarketcap.com/"
DATA_ORIGIN = "data/coinmarket.sqlite"
VALID_COINS = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "USDC", "SOL", "TRON", "DOGE"]