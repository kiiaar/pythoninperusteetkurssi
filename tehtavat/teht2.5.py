#yksi luoti 13.3g
#yksi naula on 32 luotia
#yksi leiviskä on 20 naulaa

print("Kertoisitko massan keskiaikaisten mittojen mukaan, niin muutan sen kilokrammoiksi?")

luoti = float(input("Anna luodit: "))
naula = float(input("Anna naulat: "))
leiviska = float(input("Anna leiviskät: "))

luotig = float(luoti * 13.3)
naulag = float(naula * 32 * 13.3)
leiviskag = float(leiviska * 20 * 32 * 13.3)

kilogram = (luotig + naulag + leiviskag) / 1000

print("Massa nykymittojen mukaan on: ", kilogram, "kilogrammaa")

