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


# Pääohjelma
hissi1 = Hissi(0, 7)
print("Nyt olemme kerroksessa: ", hissi1.kerros)

# Liikutaan hissillä ensin viidenteen kerrokseen. Sen jälkeen alimpaan kerrokseen.
hissi1.siirryKerrokseen(5)
print("Hissi siirtyi kerrokseen: ", hissi1.kerros)
hissi1.siirryKerrokseen(hissi1.alinKerros)
print("Hissi siirtyi alimpaan kerrokseen: ", hissi1.kerros)
