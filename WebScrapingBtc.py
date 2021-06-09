from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
from BitcoinPredict.ConnectMysql import insertBtc

def informacionBtcOnline():
    pagina = requests.get('https://www.eleconomista.es/cruce/BTCEUR')
    soup = BeautifulSoup(pagina.content, 'html.parser')
    div = soup.find("div", {"class": "col-lg-3 col-md-3 col-12"})
    precioBtc = div.text
    precioBtc = [float(s) for s in re.findall(r'-?\d+\.?\d*', precioBtc)]
    precioBtc = int(precioBtc[0])
    fecha = datetime.today().strftime('%Y-%m-%d')
    insertBtc(fecha, precioBtc)