# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin
# (esimerkiksi FI) ja tulostaa kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava
# tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='wauwii321',
    autocommit=True
    )

def searchByMaatunnus(maakoodi):
    sql = "SELECT type, count(type) from airport where iso_country = '\"" + maakoodi + "\"'group by type order by count(type) asc;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i[0], i[1])

maakoodi = input("Syötä maakoodi (esim. 'FI'): ")
searchByMaatunnus(maakoodi)