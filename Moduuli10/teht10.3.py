class Talo:
    def __init__(self, alinKerros, ylinKerros, hissiLKM):
        self.hissit = []
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.hissiLKM = hissiLKM

        for i in range(hissiLKM):
            self.hissit.append(Hissi(alinKerros, ylinKerros, i + 1))

    def print_data(self):
        print(f"\nTalon ylin kerros: {self.ylinKerros}")
        print(f"Talon alin kerros: {self.alinKerros}")
        print(f"Hissien lukumäärä: {self.hissiLKM}")

        for i in self.hissit:
            i.print_info()

    def aja_hissia(self, hissiNumero, kohdekerros):
        elevator = self.hissit[hissiNumero - 1]
        print(f"Ajetaan hissiä {hissiNumero}\n")
        elevator.go_to_floor(kohdekerros)

# Ei toimi
    def palohälytys(self):
        Hissi.go_to_floor(1)

"""Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa
 on parametriton metodi palohälytys, joka käskee kaikki hissit
  pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys."""




class Hissi:
    def __init__(self, alin, ylin, numero):
        self.nbr = numero
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def print_info(self):
        print(f"\nHissi {self.nbr}: ")
        print(f"Hissin ylin kerros: {self.ylin}")
        print(f"Hissin alin kerros: {self.alin}")
        print(f"Hissin nykyinen kerros: {self.nykyinen}\n")

    def go_to_floor(self, kerros):

        if self.alin > kerros > self.ylin:
            self.nykyinen = self.nykyinen

        elif self.alin <= kerros <= self.ylin:

            if self.nykyinen < kerros:
                x = self.alin

                while x <= kerros:
                    Hissi.floor_up(self, kerros)
                    x = x + 1

            elif self.nykyinen > kerros:
                x = self.ylin

                while x >= kerros:
                    Hissi.floor_down(self, kerros)
                    x = x - 1

    def floor_up(self, kerros):
        if self.nykyinen < kerros:
            self.nykyinen = self.nykyinen + 1
            print(f"Hissi nro{self.nbr} on kerroksessa: {self.nykyinen}")

    def floor_down(self, kerros):
        if self.nykyinen > kerros:
            self.nykyinen = self.nykyinen - 1
            print(f"Hissi nro{self.nbr} on kerroksessa: {self.nykyinen}")


if __name__ == '__main__':
    lowest_floor = 1
    top_floor = 50
    hissi_lkm = 5

    house = Talo(lowest_floor, top_floor, hissi_lkm)
    house.print_data()

    elevator_to_drive = 2
    floor_to_go = 15

    house.aja_hissia(elevator_to_drive, floor_to_go)
    house.print_data()

    house.palohälytys()
    house.print_data()