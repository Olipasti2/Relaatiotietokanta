import mysql.connector
from geopy import distance


def haelentoasema(koodi):
    tuple = (koodi, )
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;'
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos


yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

asema1 = input('Syötä ensimmäisen lentoaseman koodi:\n')
asema2 = input('Syötä toisen lentoaseman koodi:\n')

koord1 = haelentoasema(asema1)
koord2 = haelentoasema(asema2)

etaisyys = distance.distance(koord1, koord2).km

print(f'kenttien välinen etäisyys on {etaisyys:.2f}km.')
