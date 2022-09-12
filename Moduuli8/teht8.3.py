# Kirjoita ohjelma, joka kysyy käyttäjältä kahden
# lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien
# välisen etäisyyden kilometreinä. Laskenta perustuu
# tietokannasta haettuihin koordinaatteihin. Laske
# etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='wauwii321',
    autocommit=True
    )

def ICAOT():
    sql = "SELECT latitude_deg, longtitude_deg FROM airport WHERE "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i)

koodit = []

user = input("Syötä 1. ICAO-koodi: ")
koodit.append(user)

user2 = input("Syötä 2. ICAO-koodi: ")
koodit.append(user2)

ICAOT(user, user2)