pituus = float(input("Ilmoita kuhan pituus senttimetreinä: "))
if pituus < 37:
    print(f"Laske kuha takaisin järveen, se on {37 - pituus:.1f}cm alimittainen.")
else:
    print("Hieno kuha!")