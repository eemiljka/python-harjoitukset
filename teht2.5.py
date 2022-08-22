# math.floor(grammat/1000)

# luoti 13,3 g
# naula = 425,6 g
# leiviskä = 8512 g

leiviska = float(input("Anna leiviskät"))
naula = float(input("Anna naulat"))
luoti = float(input("Anna luodit"))

naula2 = (leiviska * 20) + naula
luoti2 = (naula2 * 32) + luoti
gramma = (luoti2 * 13.3)

kilogramma = gramma // 1000
gramma2 = gramma % 1000

print(f"Massa nykymittojen mukaan: ")
print(f"{kilogramma:.0f} kilogrammaa ja {gramma2:.2f} grammaa.")
