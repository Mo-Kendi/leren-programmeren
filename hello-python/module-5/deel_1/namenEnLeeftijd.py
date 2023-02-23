def print_age_and_name():
    name = input("Wat is uw naam?  ").lower()
    age = input("wat is uw leeftijd? ")
    return{ "naam":name, "leeftijd":age}
    #je maakt een functie die 2 vragen stelt en dan een dictionary die de name and age returend
personen = []
while True:
    antwoord = print_age_and_name()
    extra_naam = input("wilt u nog een naam toevoegen?").lower()
    personen.append(antwoord)    
    if extra_naam == "nee":
        break

for persoon in personen:
    print(f"Je naam is {persoon['naam']}")
