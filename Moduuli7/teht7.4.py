user = input("Syötä uusi lentoasema ('1'), hae aiempaa lentoasemaa('2') tai lopeta ('Enter') ")
icaoNimi = {"EFHK":"Helsinki-Vantaa",
            "KJFK":"JFK",
            "1234":"Lentokenttä"}
while user != 3:

    if user == "1":
        uusiKoodi = input("Syötä uusi ICAO--koodi: ").upper()
        lentokenttä = input("Syötä lentoaseman nimi: ")
        icaoNimi[uusiKoodi] = lentokenttä

    elif user == "2":
        ICAO = input("Syötä ICAO-koodi: ")
        if ICAO in icaoNimi:
            print(f"ICAO-koodi {ICAO} vastaa lentokenttää: {icaoNimi[ICAO]}")

    user = input("Syötä uusi lentoasema ('1'), hae aiempaa lentoasemaa('2') tai lopeta ('Enter') ")