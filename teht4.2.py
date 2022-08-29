# Kirjoita ohjelma, joka muuntaa tuumia
# senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma
# lopettaa toimintansa.
tuuma = float(input("Anna tuumamäärä: "))
senttimetri = tuuma * 2.54
if tuuma >= 0:
    print(f"{tuuma} tuumaa muunnettuna senttimetreiksi on {senttimetri} senttimetriä")
else:
    print("Toiminta lopetettu.")