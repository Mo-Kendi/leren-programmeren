import random
namen = [] #lege list voor namen
lootjes = {}
while True: #loop tot dat de gebruiker klaar is met namen
    naam = input("Wat zijn de namen van de spelers?  ").lower()
    if naam in namen:
        print("dit heeft u al gekozen")
    else:
        namen.append(naam) #namen toevoegen aan list
    if len(namen) >= 3:
        vraag = input("wilt u nog een naam invoeren ? ") #vragen of gebruiker meer namen inwilt vullen
        if vraag == "nee":
            break #ga uit de loop als de gebruiker klaar is met namen
shuffling = True
while shuffling:
    namen_shuffle = random.sample(namen, len(namen)) #gebruik maken van random.sample om namen te shuffelen
    shuffling = False
    for i in range(len(namen)):
        if namen_shuffle[i] == namen[i]:
            shuffling = True

for i in range(len(namen)):
    lootjes.update({namen[i]: namen_shuffle[i]})

print(lootjes) #print die namen maar !!