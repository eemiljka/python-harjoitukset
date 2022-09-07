# Kirjoita funktio, joka saa parametrinaan bensiinin
# määrän Yhdysvaltain nestegallonoina ja palauttaa
# paluuarvonaan vastaavan litramäärän. Kirjoita
# pääohjelma, joka kysyy gallonamäärän käyttäjältä
# ja muuntaa sen litroiksi. Muunnos on tehtävä
# aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen
# saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def bensa(gallon):
    litra = gallon / 0.264172052
    return litra

amount = float(input("Anna gallonamäärä: "))

while amount > 0:
    gallon_2 = bensa(amount)
    print(f"Litroissa {gallon_2}")
    amount = float(input("Anna gallonamäärä: "))