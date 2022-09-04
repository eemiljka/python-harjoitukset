# Ohjelma kysyy käyttäjätunnusta ja salasanaa.
# Mikäli käyttäjä tietää käyttäjätunnuksen: python
# ja salasanan: rules, kirjautuminen onnistuu.
# Mikäli käyttäjä ei onnistu 5 yrittämällä syöttämään
# oikeita tietoja, sisäänkirjautuminen epäonnistuu.

käyttäjätunnus = "python"
salasana = "rules"
käyttäjätunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
väärät_kerrat = 0

while käyttäjätunnus != "python" or salasana != "rules":
    väärät_kerrat += 1
    if väärät_kerrat >= 5:
        print("Sisäänkirjautuminen epäonnistui.")
        break
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
if käyttäjätunnus == "python" and salasana == "rules":
    print("Sisäänkirjautuminen onnistui!")
