joukko = set()

while True:
    user = (input("Syötä nimi: "))
    user = user.lower()
    if user not in joukko and user != "":
        print("Uusi nimi.")
        joukko.add(user)

    elif user in joukko:
        print("Aiemmin syötetty nimi.")

    if user == "":
        break

for x in joukko:
    print(x)