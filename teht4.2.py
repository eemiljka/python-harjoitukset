# ohjelma muuntaa annetut tuumat senttimetreiksi,
# kunnes käyttäjä syöttää negatiivisen luvun
# -> silloin ohjelma lopettaa toimintanta

while True:
    kysymys = float(int(input("Anna tuumat: ")))
    senttimetrit = kysymys * 2.54
    if kysymys >= 0:
        print(f"{senttimetrit} cm")
    else:
        print("Toiminto lopetettu.")
        break
