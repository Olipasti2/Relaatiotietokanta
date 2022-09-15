import mysql.connector


def haelentoasema(koodi):
    tuple = (koodi, )
    sql = f'SELECT name, municipality FROM airport WHERE ident = %s;'
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

icao = input('Syötä hakemasi lentokentän ICAO-koodi:\n')
asema = haelentoasema(icao)
if asema is not None:
    print(f'Lentokentän nimi on {asema[0]} ja sijainti on {asema[1]}')
else:
    print(f'Koodilla {icao} ei löydy lentokenttää.')