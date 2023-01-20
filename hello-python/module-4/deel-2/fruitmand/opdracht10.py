from fruitmand import fruitmand
from operator import itemgetter
# sorteer fruitmand (gewicht)
fruitmand = sorted(fruitmand , key = itemgetter("weight"),reverse=True)
for fruit in fruitmand:
        print(fruit["weight"])
    
   