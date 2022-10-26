# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden
# muutos on negatiivinen, auto hidastaa. Metodin on muutettava
# auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa
# huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka
# pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta
# uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        while self.tamanhetkinen_nopeus >= 0 and self.tamanhetkinen_nopeus <= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
            if self.tamanhetkinen_nopeus >= self.huippunopeus:
                self.tamanhetkinen_nopeus = 148
                break

    def jarruta(self, nopeuden_muutos):
        if self.tamanhetkinen_nopeus >= 0:
            self.tamanhetkinen_nopeus = 0

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus on: {auto.tamanhetkinen_nopeus}")
auto.jarruta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.tamanhetkinen_nopeus}")

