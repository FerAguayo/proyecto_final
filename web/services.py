import requests
from config import API_KEY, API_URL_BASE

SIMBOLOS_API = {
    "EUR": "EUR",
    "BTC": "BTC",
    "ETH": "ETH",
    "USDT": "USDT",
    "BNB": "BNB",
    "XRP": "XRP",
    "USDC": "USDC",
    "SOL": "SOL",
    "TRON": "TRX",
    "DOGE": "DOGE"
}

def convertir(cantidad, from_moneda, to_moneda):
    from_moneda = SIMBOLOS_API.get(from_moneda, from_moneda)
    to_moneda = SIMBOLOS_API.get(to_moneda, to_moneda)
    url = API_URL_BASE + "v2/tools/price-conversion"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }
    parametros = {
        "amount": cantidad,
        "symbol": from_moneda,
        "convert": to_moneda
    }
    try:
        respuesta = requests.get(url, headers=headers, params=parametros)
        datos = respuesta.json()
        precio = datos["data"][0]["quote"][to_moneda]["price"]
        return precio
    except Exception as e:
        return None