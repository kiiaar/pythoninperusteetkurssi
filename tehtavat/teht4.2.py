print("Kerro mitta tuumissa, muutan ne senttimetreiksi. Negatiivinen mitta lopettaa ohjelman.")

while True:
    tuumat = int(input("Mitta tuumissa: "))
    if tuumat > 0:
        print(f"Mitta senteissä: {tuumat * 2.54} cm")
    else:
        break
print("Ohjelma päättyi.")