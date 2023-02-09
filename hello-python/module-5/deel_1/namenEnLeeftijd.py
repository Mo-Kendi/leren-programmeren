def print_age_and_name():
    name = input("Wat is uw naam?  ").lower()
    age = input("wat is uw leeftijd")
    return{ "name":name, "age":age}
    #je maakt een functie die 2 vragen stelt en dan een dictionary die de name and age returend
personen = []
while True:
    antwoord = print_age_and_name()
    naam2 = input("wilt u nog een naam toevoegen?").lower()
    personen.append(antwoord)    
    if naam2 == "nee":
        break

for persoon in personen:
    print(persoon['name'], 'is', persoon["age"], 'jaar')

    