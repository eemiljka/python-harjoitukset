import random

def parittomat_poistaja(numList):
    num = 0
    parilliset = []
    while num < len(numList):

        if numList[num] % 2 == 0:
            parilliset.append(numList[num])

        num = num + 1

    return parilliset

if True:
    list = random.sample(range(1, 100), 10)
    print(f"Alkuperäinen lista: {list}")
    print(f"Lista ilman parittomia lukuja: {parittomat_poistaja(list)}")
