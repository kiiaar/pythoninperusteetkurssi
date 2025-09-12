vuosiluku = int(input("Kerro jokin vuosiluku, niin kerron sinulle onko se karkausvuosi: "))
if vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
    print("Vuosi on karkausvuosi")
elif vuosiluku % 4 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")