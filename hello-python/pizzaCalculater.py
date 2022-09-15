# Mohamad kendi pizza calculater
print('welkom bij pizza mo kendi')

small = float(6.99)
medium = float(10.99)
large = float(16.99)

smallsize = int(input("Hoeveel kleine pizza's wilt u? "))
mediumsize = int(input("Hoeveel medium pizza's wilt u hebben? "))
largesize = int(input("Hoeveel large pizza's wilt u? "))

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
