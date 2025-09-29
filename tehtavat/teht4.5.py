kerta = 0

while True:
    kayttaja = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if kayttaja != "python" and salasana != "rules":
        kerta += 1
    if kayttaja == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    if kerta == 5:
        print("Pääsy evätty")
        break
