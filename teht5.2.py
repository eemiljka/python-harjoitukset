# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen
# saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
# lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi
# reverse=True.

luvut = []

luku = int(input("Anna ensimmäinen luku: "))
while luku != "":
    luvut.append(luku)
    luku = int(input("Anna seuraava luku: "))
print(luvut)