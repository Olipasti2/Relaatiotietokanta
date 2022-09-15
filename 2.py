import mysql.connector


def haelentoasemat(maa, asematyyppi):
    tuple = (maa, asematyyppi)
    sql = f'SELECT COUNT(type) FROM AIRPORT WHERE iso_country = %s AND type=%s;'
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos


def haetyypit():
    sql = f'SELECT DISTINCT type FROM AIRPORT;'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

maakoodi = input('Syötä maakoodi:\n')
tyypit = haetyypit()
for tyyppi in tyypit:
    print(haelentoasemat(maakoodi, tyyppi[0]), tyyppi[0])
