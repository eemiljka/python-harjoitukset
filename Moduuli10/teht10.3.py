# KOODI EI TOIMI

# Luodaan hissi-luokka, jolla 3 metodia: Siirry kerrokseen, kerros ylös ja kerros alas.
class Hissi:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.kerros = self.alinKerros

    def siirryKerrokseen(self, uusiKerros):
        if uusiKerros > self.kerros:
            while self.kerros < uusiKerros:
                hissi1.kerrosYlös()
        elif uusiKerros < self.kerros:
            while self.kerros > uusiKerros:
                hissi1.kerrosAlas()


    def kerrosYlös(self):
        self.kerros = self.kerros + 1

    def kerrosAlas(self):
        self.kerros = self.kerros - 1

class Talo:
    def __init__(self, talonAlin, talonYlin, hissienLKM):
        self.talonAlin = talonAlin
        self.talonYlin = talonYlin
        self.hissienLKM = hissienLKM
        self.hissit = []
        self.hissit.append(hissienLKM)

    def aja_hissiä(self, hissi_numero, kohdekerros):
        self.hissi_numero = hissi_numero
        self.kohdekerros = kohdekerros
        for hissi in self.hissit:
            hissi.siirryKerrokseen(kohdekerros)

    def palohälytys(self):
        self.hissit.siirryKerrokseen(0)


# Pääohjelma
hissi1 = Hissi(0, 7)
print("Nyt olemme kerroksessa: ", hissi1.kerros)

# Liikutaan hissillä ensin viidenteen kerrokseen. Sen jälkeen alimpaan kerrokseen.
hissi1.siirryKerrokseen(5)
print("Hissi siirtyi kerrokseen: ", hissi1.kerros)
hissi1.siirryKerrokseen(hissi1.alinKerros)
print("Hissi siirtyi alimpaan kerrokseen: ", hissi1.kerros)

# Luodaan talo ja lause talon hisseillä ajelemiseksi
talo1 = Talo(0, 7, 1)
talo1.aja_hissiä(0, 7)

