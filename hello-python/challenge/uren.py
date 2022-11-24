# uur = int(input('hoe laat is het in uren?'))
# minuut = int(input('hoe laat is het in minuten?'))
# tijd = uur + minuut
# print(tijd)
# print(f'voor dat de dag voor bij is duurt het nog {tijd} uur')
#dit was eerst wat ik had

uur = 23
min = 60
tijdnu = int(input('hoe laat is het in uren?'))
minuutnu = int(input('hoe laat is het in minuten?'))

eindtijd = uur - tijdnu
eindmin = 60 - minuutnu

print(f'dan duurt de dag nog {eindtijd} uur en {eindmin} minuten')
