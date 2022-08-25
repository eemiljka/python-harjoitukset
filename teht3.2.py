# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja
# tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä
# on käytettävä if/elif/else-toistorakennetta.
#
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
hyttiluokka = input("Mikä on hyttiluokkasi? ")
if hyttiluokka in ["LUX"] or ["lux"]:
    print("LUX on parvekkeellinen hytti yläkannella.")
if hyttiluokka in ["A"] or ["a"]:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
if hyttiluokka in ["B"] or ["b"]:
    print("B on ikkunaton hytti autokannen yläpuolella.")
if hyttiluokka in ["C"] or ["c"]:
    print("C on ikkunaton hytti autokannen alapuolella.")

