# Ohjelma ilmoittaa onko kalastettu kuha
# alimittainen, ja kuinka paljon.

kuha_pituus = float(input("Anna kuhan pituus (cm): "))
sallittu_pituus = 37 * -1
if kuha_pituus<37:
    print("\nLaske kuha takaisin veteen. Kuha on alimittainen.")
    print("Alimmasta sallitusta pyyntimitasta puuttuu")
    print(-1 * kuha_pituus - sallittu_pituus, "cm")
else:
    print("Kuha EI ole alimittainen.")