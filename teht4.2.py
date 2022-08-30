# Kirjoita ohjelma, joka muuntaa tuumia
# senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma
# lopettaa toimintansa.

while True:
    kysymys = float(int(input("Anna tuumat: ")))
    senttimetrit = kysymys * 2.54
    if kysymys >= 0:
        print(f"{senttimetrit} cm")
    else:
        print("Toiminto lopetettu.")
        break
