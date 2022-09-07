# Kirjoita parametriton funktio, joka palauttaa
# paluuarvonaan satunnaisen nopan silmäluvun
# väliltä 1..6. Kirjoita pääohjelma, joka heittää
# noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun
# silmäluvun.

import random
def satunnainen():
    noppaLuku = random.randint(1, 6)
    return noppaLuku

while True:
    silmäluku = satunnainen()
    print(silmäluku)
    if silmäluku == 6:
        break

