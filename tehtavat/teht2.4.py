print("Hei, kysyn sinulta kolme lukua, anna luvut kokonaislukuina.")
A = int(input("Ensimmäinen luku C: "))
B = int(input("toinen luku B: "))
C = int(input("kolmas luku C: "))

summa = A + B + C
tulo = A * B * C
keskiarvo = (A + B + C) / 3

print(f"lukujen summa on: {summa:.2f}")
print(f"lukujen tulo on: {tulo:.2f}")
print(f"keskiarvo on: {keskiarvo:.2f}")

