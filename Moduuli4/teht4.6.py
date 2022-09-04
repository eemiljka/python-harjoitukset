# Kirjoita ohjelma, joka kysyy arvottavien pisteiden
# määrän käyttäjältä ja toteuttaa piin likiarvon laskennan
# edellä kuvatulla menetelmällä. Lopuksi ohjelma tulostaa
# piin likiarvon käyttäjälle. (Huomaa, että jokaisesta
# arvotusta pisteestä (x,y) on helppoa testata onko se
# yksikköympyrän A sisällä: riittää testata, toteuttaako
# piste epäyhtälön x^2+y^2<1.)

import random

n = 0        # ympyrän sis. jäävät pisteet
B = 0        # neliön sis. jäävät pisteet
N = int(input("Anna pisteiden lukumäärä: "))

for i in range(N ** 2):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    origo_dist = rand_x ** 2 + rand_y ** 2

    if origo_dist <= 1:
        n += 1

    B += 1

    pi = 4 * n / B

print("Piin likiarvo on:",pi)