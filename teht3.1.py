# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta
# pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha_pituus = float(input("Anna kuhan pituus (cm): "))
if kuha_pituus<37:
    print("Laske kuha takaisin veteen. Kuha on alimittainen.")
    print("Alimmasta sallitusta pyyntimitasta puuttuu")
    print(kuha_pituus - 37)