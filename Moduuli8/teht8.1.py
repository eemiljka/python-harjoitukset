# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman
# ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
# lentokentän nimen ja sen sijaintikunnan kurssilla
# käytettävästä lentokenttätietokannasta.

import mysql.connector

def searchAirportsByICAO():
    sql = "SELECT name, municipality FROM airport"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)

#PÄÄOHJELMA
user = input("Syötä lentoaseman ICAO-koodi: ")
searchAirportsByICAO(user)


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='wauwii321',
    autocommit=True
    )