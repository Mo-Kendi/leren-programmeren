import random
Kleur = ["oranje","blauw","groen","bruin"]
hvlMM = int(input("Hoeveel M&M's er aan de zak toegevoegd moeten worden? "))
ZakMetMM = []

for x in range(hvlMM):
    ZakMetMM.append(random.choice(Kleur))
zak2 = {}

for zak in ZakMetMM:
    if zak in zak2:
        zak2[zak] += 1
    else:
        zak2[zak] = 1

for key, value in zak2.items():
    if value > 0:
        print(key, ":", value)
#als het boven de 0 is dan wordt t geprint