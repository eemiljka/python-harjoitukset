vuodenajat = ("kevät", "kesä", "syksy", "talvi")

while True:
    user = int(input("Syötä kuukauden numero: "))

    if user == 3 or user == 4 or user == 5:
        print(vuodenajat[0])
        break

    if user == 6 or user == 7 or user == 8:
        print(vuodenajat[1])
        break

    if user == 9 or user == 10 or user == 11:
        print(vuodenajat[2])
        break

    if user == 12 or user == 1 or user == 2:
        print(vuodenajat[3])
        break
