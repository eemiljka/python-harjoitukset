# ohjelma kysyy käyttäjältä lukuja, kunnes
# käyttäjä syöttää tyhjän merkkijonon, jolloin
# ohjelma tulostaa syöttämistä luvuista
# pienimmän ja suurimman luvun

import math

annettu_luku = input("Anna luku: ")
suurin_luku = -math.inf
pienin_luku = math.inf

while annettu_luku != "":

    luku = int(annettu_luku)

    if luku > suurin_luku:
        suurin_luku = luku

    if luku < pienin_luku:
        pienin_luku = luku

    annettu_luku = input("Anna luku: ")
if suurin_luku == -math.inf or pienin_luku == math.inf:
    print("Et syöttänyt arvoja!")

else:
    print(f"Pienin syöttämäsi luku: {pienin_luku}")
    print(f"Suurin syöttämäsi luku: {suurin_luku}")