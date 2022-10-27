# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu
# matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa
# lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random


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
    print(car.print_info())
