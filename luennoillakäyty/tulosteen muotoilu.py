#muuntaminen tapa 1
ika_str = input("kuinka vanha olet?: ")
ika = int(ika_str)

print("oh, so you were born in ", 2025 - ika)

#muuntaminen tapa 2
ika = int(input("kuinka vanha olet?: "))
print("oh, so you were born in", 2025 - ika)

#muotoiltu tuloste
print(f"oh, so you were born in {2025 - ika}.")

