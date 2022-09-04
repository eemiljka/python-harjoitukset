# Kirjoita peli, jossa tietokone arpoo kokonaisluvun
# väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen
# asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen
# ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni
# arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa
# lukuaan arvauskertojen välissä.
import random
x = random.randint (1, 10)
while True:
    print(("Arvaa luku välillä 1-10: "))
    arvaus = input()
    luku = int(arvaus)
    if luku == x:
        print("Oikein.")
        break
    elif luku < x:
        print("Kokeile suurempaa lukua: ")
    elif luku > x:
        print("Kokeile pienempää lukua: ")
