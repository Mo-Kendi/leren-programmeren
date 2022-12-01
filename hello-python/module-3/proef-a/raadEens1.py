import random

aantalRounds = 20
aantalpoginen = 10
ronde = 0
score = 0
poging = 0
raadGetal = random.randint(1, 1000)
while ronde < aantalRounds:
    meeDoen = input("zou je een getal tussen 1 en 1000 willen raden? ja/nee  ")

    if meeDoen == "nee":
        print("einde")
        print(f"Jou eind score is {score} van de {aantalRounds} punten!")
        exit()
    elif meeDoen == "ja":
        print('je gaat nu 10 keer raden en dan kijken wij of je goed hebt ')

    while poging < aantalpoginen:
        while True:
            try:
                antwoord = int(input('raad het getal: '))
                break
            except ValueError:
                print('je mag alleen cijfers')

        if raadGetal == antwoord:
            print('je hebt het getal goed geraden!')
            score+=1
            break
        else:      #De absolute waarde houdt zich bezig met de waarde of omvang van een getal in plaats van het teken dat aan het getal is gekoppeld
            verschil = abs(antwoord - raadGetal)
            if verschil <= 20:  # berekent hier of het heel dichtbij is of dichtbij
                print("Je bent heel dichtbij!")
            elif verschil <= 50 and verschil >= 20:
                print("Je bent dichtbij!")
        poging += 1

    print(f"jou eind score is{score} ")
    ronde+=1

print(f"Jou eind score is {score} van de {aantalRounds} punten!")