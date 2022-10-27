# Laajenna ohjelmaa siten, että mukana on kulje-metodi,
# joka saa parametrinaan tuntimäärän. Metodi kasvattaa
# kuljettua matkaa sen verran kuin auto on tasaisella
# vauhdilla annetussa tuntimäärässä edennyt. Esimerkki:
# auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus
# on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun
# matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if self.tamanhetkinen_nopeus >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif nopeuden_muutos < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.tamanhetkinen_nopeus * tuntimaara + self.kuljettu_matka
        print(f"Kuljettu matka: {self.kuljettu_matka}")


auto = Auto("ABC-123", 142)

auto.kiihdytä(20)
print(f"Tämän hetkinen nopeus: {auto.tamanhetkinen_nopeus}")
auto.kulje(2)

auto.kiihdytä(20)
print(f"Tämän hetkinen nopeus: {auto.tamanhetkinen_nopeus}")
auto.kulje(2)
