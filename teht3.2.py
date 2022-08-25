
hyttiluokka = input("Mikä on hyttiluokkasi? ")

if hyttiluokka in ["LUX"]:
    print("LUX on parvekkeellinen hytti yläkannella.")
if hyttiluokka in ["A"]:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
if hyttiluokka in ["B"]:
    print("B on ikkunaton hytti autokannen yläpuolella.")
if hyttiluokka in ["C"]:
    print("C on ikkunaton hytti autokannen alapuolella.")

# NÄITÄ VIKOJA RIVEJÄ EN SAANUT TOIMIMAAN...
# else:
#     print("Virheellinen hyttiluokka.")