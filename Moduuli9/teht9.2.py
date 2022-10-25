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
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus, kuljettu_matka, nopeuden_muutos):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        self.nopeuden_muutos = nopeuden_muutos

    def kiihdytä(self, nopeuden_muutos):
        self.nopeuden_muutos = 0
        self.nopeuden_muutos += 30
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + self.nopeuden_muutos
        if self.tamanhetkinen_nopeus < self.huippunopeus:
            self.nopeuden_muutos += 70
            self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + self.nopeuden_muutos
        else:
            print(self.tamanhetkinen_nopeus)
            if self.tamanhetkinen_nopeus < self.huippunopeus:
                self.nopeuden_muutos += 50
                self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + self.nopeuden_muutos
            else:
                print(self.tamanhetkinen_nopeus)
                if self.tamanhetkinen_nopeus <


auto = Auto("ABC-123", 142, 0, 0)

def autontulostus():
    print(f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.tamanhetkinen_nopeus}, {auto.kuljettu_matka}")

autontulostus()