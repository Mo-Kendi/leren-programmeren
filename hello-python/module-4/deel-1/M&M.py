import random
kleuren = ["oranje","blauw","groen","bruin"]
hvlMM = int(input("Hoeveel M&M's er aan de zak toegevoegd moeten worden? "))
zakMM = []
for x in range(hvlMM):
    zakMM += random.choices(kleuren)

print(zakMM)