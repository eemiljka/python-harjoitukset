# Kirjoita ohjelma, joka kysyy käyttäjältä
# lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Lopuksi
# ohjelma tulostaa saaduista luvuista
# pienimmän ja suurimman.
luku = input("Anna luku: ")
pienin_luku = min(luku)
suurin_luku = max(luku)
while luku != "":
    luku = input("Anna luku: ")
    if luku == "":
        print(pienin_luku, suurin_luku)
# ei ihan toimi oikealla tavalla.