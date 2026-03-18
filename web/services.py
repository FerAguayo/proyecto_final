import requests
from config import API_KEY, API_URL_BASE

def convertir(cantidad, from_moneda, to_moneda):
    url = API_URL_BASE + "v2/tools/price-conversion"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }
    parametros = {
        "amount": cantidad,
        "symbol": from_moneda,
        "convert": to_moneda
    }
    respuesta = requests.get(url, headers=headers, params=parametros)
    datos = respuesta.json()
    precio = datos["data"][0]["quote"][to_moneda]["price"]
    return precio