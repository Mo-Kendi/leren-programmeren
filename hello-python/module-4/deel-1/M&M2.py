import random
kleur = ["oranje","blauw","groen","bruin"]
hvlMM = int(input("Hoeveel M&M's er aan de zak toegevoegd moeten worden? "))
zakMM = []

for y in range(hvlMM):
    zakMM.append(random.choice(kleur))
zak2 = {}

for x in zakMM:
    if x in zak2:
        zak2[x] += 1
    else:
        zak2[x] = 1

for key, value in zak2.items():
    if value > 0:
        print(key, ":", value)
#als het boven de 0 is dan wordt t geprint