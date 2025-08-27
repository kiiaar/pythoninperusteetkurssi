pituus = int(input("anna pituutesi: "))
paino = float(input("anna painosi: "))

#muuttuja jossa lasku suoritetaan
bmi = paino / (pituus/100) ** 2

print("painoindeksisi on: ", bmi)

#muotoiltu kahteen desimaaliin
print(f"pituuspainoindeksisi on: {bmi:.2f}")
