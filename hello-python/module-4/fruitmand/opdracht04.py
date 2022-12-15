from fruitmand import fruitmand
import random
aantal = int(input('Hoeveel?'))
for x in range(aantal):
    print(random.choice(fruitmand)['name'])