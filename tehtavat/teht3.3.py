sukupuoli = input("Kertoisitko biologisen sukupuolesi: ")
arvo = int(input("Ja kertoisitko vielä gemoglobiiniarvosi: "))

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= arvo <= 175:
        print("Hemoglobiniarvosi on normaalilla tasolla.")
    elif arvo > 175:
        print("Hemoglobiiniarvosi on korkea")

elif sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= arvo <= 195:
        print("Hemoglobiniarvosi on normaalilla tasolla.")
    elif arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")

