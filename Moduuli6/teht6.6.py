import math

def pizza_laskin(pizza_halkaisija_cm, pizza_hinta):
    pizza_ala_cm2 = math.pi / 4 * pizza_halkaisija_cm ** 2
    pizza_ala_m2 = pizza_halkaisija_cm * 0.01 * 0.01
    pizza_hinta_m2 = pizza_hinta / pizza_ala_m2
    return pizza_hinta_m2

if True:
    pizza1halk_cm = float(input("1. pizzan halkaisija (cm): "))
    pizza1hint = float(input("1. pizzan hinta: "))
    pizza2halk_cm = float(input("2. pizzan halkaisija (cm): "))
    pizza2hint = float(input("2. pizzan hinta: "))

    pizza1 = pizza_laskin(pizza1halk_cm, pizza1hint)
    pizza2 = pizza_laskin(pizza2halk_cm, pizza2hint)

    if pizza1 > pizza2:
        print("2. pizza on neliöhinnaltaan parempi.")

    else:
        print("1. pizza on neliöhinnaltaan parempi.")