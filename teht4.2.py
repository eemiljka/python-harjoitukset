# Kirjoita ohjelma, joka muuntaa tuumia
# senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma
# lopettaa toimintansa.
tuuma2 = ""

while tuuma2 != "lopeta":
    tuuma2 = float(input("Anna tuumamäärä: "))
    print(f"{tuuma2} tuumaa muunnettuna senttimetreiksi on {tuuma2 * 2.54} cm")
else:
    print("Ohjelma lopetettu")