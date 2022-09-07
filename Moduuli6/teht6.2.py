# Muokkaa edellistä funktiota siten,
# että funktio saa parametrinaan nopan
# tahkojen yhteismäärän. Muokatun funktion
# avulla voit heitellä esimerkiksi 21-tahkoista
# roolipelinoppaa. Edellisestä tehtävästä poiketen
# nopan heittelyä jatketaan pääohjelmassa kunnes
# saadaan nopan maksimisilmäluku, joka kysytään
# käyttäjältä ohjelman suorituksen alussa.

import random

def satunnainen(tahkot):
    noppaLuku = random.randint(1, tahkot)
    return noppaLuku

TahkoLKM = int(input("Kuinka monta tahkoa? "))

while True:
    silmäluku = satunnainen(TahkoLKM)
    print(silmäluku)
    if silmäluku == TahkoLKM:
        break