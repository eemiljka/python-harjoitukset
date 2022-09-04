# ohjelmalle syötetään vuosiluku, ja se ilmoittaa onko kyseinen vuosi karkausvuosi vai ei

vuosi = float(input("Anna vuosiluku: "))
if vuosi % 400 == 0 or vuosi % 100 != 0 and vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")