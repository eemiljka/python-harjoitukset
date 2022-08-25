# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja
# hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen,
# normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
sukupuoli = input("Oletko mies vai nainen: ")
if sukupuoli in ["nainen"]:
    arvo1 = float(input("Kerro hemoglobiiniarvosi (g/l): "))
    if 117 <= arvo1 <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    if arvo1<117:
        print("Hemoglobiiniarvosi on alhainen.")
    if arvo1>175:
        print("Hemoglobiiniarvosi on korkea.")
if sukupuoli in ["mies"]:
    arvo2 = float(input("Kerro Hemoglobiiniarvosi (g/l: "))
    if 134 <= arvo2 <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    if arvo2<134:
        print("Hemoglobiiniarvosi on alhainen.")
    if arvo2>195:
        print("Hemoglobiiniarvosi on korkea.")
