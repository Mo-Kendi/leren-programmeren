import random
Kleur = ["oranje","blauw","groen","bruin"]
hvlMM = int(input("Hoeveel M&M's er aan de zak toegevoegd moeten worden? "))
ZakMetMM = []
for x in range(hvlMM):
    ZakMetMM += random.choices(Kleur)

print(ZakMetMM)