matchWin = 3
matchLose = 0
land1 = input ('welke land speelt eerst in groep A? ')
land2 = input ('welke land speelt als tweede in groep A? ')
land3 = input ('welke land speelt als derde in groep A? ')
groepA = [land1,land2,land3,]
#print(groepA)

print (f'''
wedstrijden     thuis       uit         Doelpunten1         Doelpunten2         winnaar
1               {land1}     {land2}     
2               {land2}     {land3}
3               {land1}     {land3}''')

