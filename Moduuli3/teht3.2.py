hyttiluokka = input("Mikä on hyttiluokkasi? ")
if hyttiluokka in ["LUX"]:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka in ["A"]:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka in ["B"]:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka in ["C"]:
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")