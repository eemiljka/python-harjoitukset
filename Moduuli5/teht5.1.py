import random

def main():
    while True:
        nopat = int(input("Montaako noppaa heitetään: "))
        if nopat < 1:
            print("Vähimmäins noppamäärä on 1. Yritä uudelleen: ")
        else:
            break
    tulos = heitto(nopat)
    print(f"Summa {nopat} nopalle on {tulos}.")


def heitto(nopat):
    heitot = 0
    for i in range(1, nopat + 1):
        print(f"Heitto #{i} = {(heitto2 := random.randint(1, 6))}")
        heitot += heitto2
    return heitot

main()