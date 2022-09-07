# Kirjoita funktio, joka saa parametrinaan listan
# kokonaislukuja. Ohjelma palauttaa listassa olevien
# lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen
# palauttaman summan.
import random
def numList(luvut):
    summa = sum(luvut)
    return summa

if True:
    lista = random.sample(range(1,100), 10)
    print(f"Listan summa: {numList(lista)}")