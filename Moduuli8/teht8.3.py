# Kirjoita ohjelma, joka kysyy käyttäjältä kahden
# lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien
# välisen etäisyyden kilometreinä. Laskenta perustuu
# tietokannasta haettuihin koordinaatteihin. Laske
# etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='wauwii321',
    autocommit=True
    )

def ICAOT(ICAOGPS):
    sql = "SELECT latitude_deg, longtitude_deg FROM airport WHERE gps_code = '" + ICAOGPS + "';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

user = input("Syötä 1. ICAO-koodi: ")
lentoasema1 = ICAOT(user)

user2 = input("Syötä 2. ICAO-koodi: ")
lentoasema2 = ICAOT(user2)
print(f"{distance.distance(lentoasema1, lentoasema2).km:.2f}")
