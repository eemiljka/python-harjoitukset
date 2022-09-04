# Ohjelma tulostaa kolmella jaolliset
# luvut väliltä 1-1000
pienin_luku = 0
while pienin_luku < 1000:
    pienin_luku = pienin_luku + 1
    if pienin_luku % 3 == 0:
        print(pienin_luku)