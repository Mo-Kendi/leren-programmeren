# Mohamad kendi pizza calculater
from tkinter import E


print('welkom bij pizza mo kendi')

small = 6.99
medium = float(10.99)
large = float(16.99)
ex = 0

while ex == 0:
    try:
        smallsize = int(input("Hoeveel kleine pizza's wilt u? "))
        ex = 1
    except:
        print('onjuiste ingevoerde waarde')

ex = 0
while ex == 0:
    try:   
        largesize = int(input("Hoeveel large pizza's wilt u? "))
        ex = 1
    except:
        print('onjuiste ingevoerde waarde')

ex = 0
while ex == 0:
    try:
        mediumsize = int(input("Hoeveel medium pizza's wilt u hebben? "))
        ex = 1
    except:
        print('onjuiste ingevoerde waarde')


totaal = smallsize * small + mediumsize * medium + largesize * large
totaal_af = round(totaal,2)
print(f"""U heeft in totaal {smallsize} small pizza's, {mediumsize} medium pizza's en
{largesize} large pizza's besteld, Het wordt dan in totaal €{totaal_af}""")

print(f'''|-----------------------------------------------------|
|                        Bon                          |
|                                                     |
|Small pizza {smallsize} x {small}                                 | 
|                                                     |
|Medium pizza {mediumsize} x {medium}                               |
|                                                     |
|Large pizza {largesize} x { large}                                |
|                                                     |
|                                              Totaal |
|                                              {totaal_af} |
|-----------------------------------------------------|''')
