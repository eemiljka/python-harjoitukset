import random
# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina
# kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän
# ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

class Kilpailu:
    def __init__(self):
        self.kilpailun_nimi = "Suuri Romuralli"
        self.kilpailun_pituus = 8000
        self.autolista = []

    def tunti_kuluu(self):


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

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


cars = []
for i in range(10):
    cars.append(Auto("ABC-" + str(i + 1), random.randint(100, 200)))

stop = False
while not stop:
    for car in cars:
        car.kiihdytä(random.randint(-10, 15))
        car.kulje(1)
        if car.kuljettu_matka >= 10000:
            stop = True
            break

for car in cars:
    (car.print_info())
