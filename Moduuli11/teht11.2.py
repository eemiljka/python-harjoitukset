class Kilpailu:
    def __init__(self):
        self.kilpailun_nimi = "Suuri Romuralli"
        self.kilpailun_pituus = 8000
        self.autolista = []


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

class Electric(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, batteryCapacity):
        self.batteryCapacity = batteryCapacity
        super().__init__(rekisteritunnus, huippunopeus)
        self.tamanhetkinen_nopeus = 100
    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.tamanhetkinen_nopeus * tuntimaara + self.kuljettu_matka
    def print_info(self):
        print(f"Auton {self.rekisteritunnus} "
              f"huippunopeus on {self.huippunopeus} km/h, "
              f"matkamittari: {self.kuljettu_matka} km, "
              f"tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h.")

class Combustion(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, gasolineTank):
        self.gasolineTank = gasolineTank
        super().__init__(rekisteritunnus, huippunopeus)
        self.tamanhetkinen_nopeus = 80

    def print_info(self):
        print(f"Auton {self.rekisteritunnus} "
              f"huippunopeus on {self.huippunopeus} km/h, "
              f"matkamittari: {self.kuljettu_matka} km, "
              f"tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h.")

    def kiihdytä(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if self.tamanhetkinen_nopeus >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif nopeuden_muutos < 0 and nopeuden_muutos > -10:
            self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.tamanhetkinen_nopeus * tuntimaara + self.kuljettu_matka

car1 = Electric("ABC-15", 180, 52.5)
car2 = Combustion("ACD-123", 165, 32.3)

car1.kulje(3)
car2.kulje(3)

car1.print_info()
car2.print_info()
