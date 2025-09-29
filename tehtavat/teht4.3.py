
luku = input("Kirjoita jokin luku, lopeta ohjelma tyhjällä merkkijonolla: ")
isoin = luku
pienin = luku
while luku != "":
    luku = input("Kirjoita seuraava luku, lopeta ohjelma tyhjällä merkkijonolla: ")
    if pienin > luku and luku != "":
        pienin = luku
    if isoin < luku:
        isoin = luku
    if luku == "":
        print(f"{pienin}, {isoin}")
        break

