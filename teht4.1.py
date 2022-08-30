# Kirjoita while-toistorakennetta
# käyttävä ohjelma,
# joka tulostaa kolmella jaolliset
# luvut väliltä 1..1000.
pienin_luku = 1
suurin_luku = 1000
for luvut in range(pienin_luku, suurin_luku + 1):
    if luvut%3==0:
        print(luvut)