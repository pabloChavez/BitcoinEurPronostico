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


def insertBtc(fecha, precioBtc):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  database='bitcoin')
    cursor = cnx.cursor()
    sql = "INSERT INTO bitcoinshist (fecha, euro) VALUES (%s, %s)"
    val = (fecha, precioBtc)
    cursor.execute(sql, val)
    cnx.commit()


def insertDatosFinales(puntuaciontrain, puntuaciontest, proximodia):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  database='bitcoin')
    cursor = cnx.cursor()
    sql = "INSERT INTO datosfinales (puntuaciontrain, puntuaciontest, proximodia, fecha) VALUES (%s, %s, %s, %s)"
    fecha = datetime.today().strftime('%Y-%m-%d')
    val = (puntuaciontrain, puntuaciontest, proximodia, fecha)
    cursor.execute(sql, val)
    cnx.commit()
