
print('Beantwoord de vragen vervolgens maak een keus')
iphone = float(input('Hoe duur is de iphone telefoon? '))
samsung = float(input('Hoe duur is de samsung telefoon? '))

verschill = iphone - samsung
verschill2 = samsung - iphone
if iphone > samsung:
    print(f'De iPhone is het duurst, de telefoon kost: {iphone} euro')
    print(f"De samsung is het goedkoopst, de telefoon kost{samsung} euro")
    print(f"Het advies is dus de samsung te kopen, deze is namelijk {verschill} euro goedkoper dan de iphone. ")
elif samsung > iphone:
    print(f'De iPhone is het goedkoopst, de telefoon kost: {iphone} euro')
    print(f"De samsung is het duurst, de telefoon kost{samsung} euro")
    print(f"Het advies is dus de iphone te kopen, deze is namelijk {verschill2} euro goedkoper dan de samsung. ")
else:
    print("De prijzen van de Iphone en Samsung zijn gelijk, toch raden we je aan om de Iphone te kopen, deze telefoon werkt namelijk sneller.")

if verschill > 50:
    print('koop dan de s22')
elif verschill < 50:
    print('koop dan de iphone')
