user = input("Syötä uusi lentoasema ('1')\nhae aiempaa lentoasemaa('2')\ntai lopeta syöttämällä jotain muuta: ")
icaoNimi = {"EFHK":"Helsinki-Vantaa",
            "KJFK":"John F. Kennedy",
            "00NJ":"Colgate-Piscataway"}

while user == "1" or user == "2" and user != "3":

    if user == "1":
        uusiKoodi = input("Syötä uusi ICAO-koodi: ").upper()
        lentokenttä = input("Syötä lentoaseman nimi: ")
        icaoNimi[uusiKoodi] = lentokenttä

    elif user == "2":
        ICAO = input("Syötä ICAO-koodi: ").upper()
        if ICAO in icaoNimi:
            print(f"ICAO-koodi {ICAO} vastaa lentokenttää: {icaoNimi[ICAO]}")

    user = input("\nSyötä uusi lentoasema ('1')\nhae aiempaa lentoasemaa('2')\ntai lopeta ('3') ")

print("Ohjelma lopetetaan.")
