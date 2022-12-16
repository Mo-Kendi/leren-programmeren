boodschappenlijst = {}
extra = "ja"
while extra == "ja":
    product = input("wat wil je toevoeg aan de boodschappenlijst ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?"))

    if product not in boodschappenlijst:
        boodschappenlijst.update({product : aantal})

    else:
        boodschappenlijst[product] += aantal
    extra = input("wil je nog meer toevoegen? ").lower()

print("boodscappenlijst")
for aantal, product in boodschappenlijst.items():
    print(f"{product} x {aantal}")