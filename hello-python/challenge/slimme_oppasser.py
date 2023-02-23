def bereken_poten(aantal_giraffen, aantal_struisvogels, aantal_zebras):
    totaal_poten = (aantal_giraffen * 4) + (aantal_struisvogels * 2) + (aantal_zebras * 4)
    return totaal_poten

aantal_giraffen = int(input("Hoeveel giraffen zijn er? "))
aantal_struisvogels = int(input("Hoeveel struisvogels zijn er? "))
aantal_zebras = int(input("Hoeveel zebras zijn er? "))

aantal_poten = bereken_poten(aantal_giraffen, aantal_struisvogels, aantal_zebras)
print(f"totale aantal poten zijn {aantal_poten}")
