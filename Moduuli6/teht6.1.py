# Kirjoita parametriton funktio, joka palauttaa
# paluuarvonaan satunnaisen nopan silmäluvun
# väliltä 1..6. Kirjoita pääohjelma, joka heittää
# noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun
# silmäluvun.

import random

def satunnainen():
    print(random.randint(1, 6))
    return

heitto = input("Syötä 'h' heittääksesi noppaa. ")
if heitto == "h":
    satunnainen()
    if satunnainen < 6:
        heitto = (input("Syötä 'h' heittääksesi noppaa. ")

