kaupungit = []
kaupunki = input("Anna kaupungin nimi: ")
kerrat = 0
while kerrat < 5:
    kerrat += 1
    kaupungit.append(kaupunki)
    kaupunki = input("Anna kaupungin nimi: ")

for i in kaupungit:
    print(i)

# kysyy 6 kertaa, printtaa 5...