# Ohjelma kysyy käyttäjältä alkulukua
# ja ilmoittaa, onko se alkuluku.

luku = int(input("Anna kokonaisluku: "))
if luku > 1:
    for i in range(2, luku):
        if (luku % i) == 0:
            print(luku, "ei ole alkuluku.")
            print(i, "kertaa", luku//i, "on", luku)
            break
    else:
        print(luku, "on alkuluku")
else:
    print(luku, "ei ole alkuluku")