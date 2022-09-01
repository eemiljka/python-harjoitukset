# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen
# saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
# lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi
# reverse=True.

lukulista = []
uusiluku = input("Syötä luku: ")

while uusiluku != "":
    lukulista.append(uusiluku)
    uusiluku = input("Syötä luku: ")

print(lukulista)