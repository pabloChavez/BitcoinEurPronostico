from datetime import datetime
import mysql.connector
from pandas import DataFrame

def coneccionDb():
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  database='bitcoin')
    cursor = cnx.cursor()
    query = ("SELECT euro FROM bitcoinshist")
    cursor.execute(query)
    query_result = list(cursor)
    dataframe = DataFrame(query_result)

    return dataframe


def insertBtc(precioBtc):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  database='bitcoin')
    cursor = cnx.cursor()
    sql = "INSERT INTO bitcoinshist (fecha, euro) VALUES (%s, %s)"
    fecha = datetime.today().strftime('%Y-%m-%d')
    val = (fecha, precioBtc)
    cursor.execute(sql, val)
    cnx.commit()


def insertDatosFinales(puntuaciontrain, puntuaciontest, pronostico):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  database='bitcoin')
    cursor = cnx.cursor()
    sql = "INSERT INTO datosfinales (puntuaciontrain, puntuaciontest, pronostico, fecha) VALUES (%s, %s, %s, %s)"
    fecha = datetime.today().strftime('%Y-%m-%d')
    val = (puntuaciontrain, puntuaciontest, pronostico, fecha)
    cursor.execute(sql, val)
    cnx.commit()


def insertCryptoMarker(compra, venta, ultPrecio):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  database='bitcoin')
    cursor = cnx.cursor()
    sql = "INSERT INTO cryptomarker (compra, venta, ultPrecio, fecha) VALUES (%s, %s, %s, %s)"
    fecha = datetime.today().strftime('%Y-%m-%d')
    val = (compra, venta, ultPrecio, fecha)
    cursor.execute(sql, val)
    cnx.commit()
