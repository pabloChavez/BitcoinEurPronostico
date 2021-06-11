from cryptomarket.exchange.client import Client
import json

from BitcoinPredict.ConnectMysql import insertCryptoMarker, insertBtc

api_key='AB32B3201'
api_secret='21b12401'
client = Client(api_key, api_secret)

bitcoin = client.get_ticker(market="BTCEUR")

bitcoin = json.dumps(bitcoin)

compra = int(bitcoin[98:103])
venta = int(bitcoin[82:87])
ultPrecio = int(bitcoin[121:126])

def informacionBtcOnline():
    insertCryptoMarker(compra, venta, ultPrecio)
    insertBtc(ultPrecio)
