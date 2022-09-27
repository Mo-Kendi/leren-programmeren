ScoreE = int(input("Hoeveel punten heb je gescoordt in ScoreE? (0-6) "))
ScoreP = int(input("Hoeveel punten heb je gescoordt in ScoreP? (0-8) "))
ScoreO = int(input("Hoeveel punten heb je gescoordt in ScoreO? (0-5) "))
ScoreS = int(input("Hoeveel punten heb je gescoordt in ScoreS? (0-2) "))

totalScore = ScoreE + ScoreP + ScoreO + ScoreS

if ScoreE == 4 and ScoreP == 8 and ScoreO == 0 and ScoreS == 0 :
    print("Je hebt GOED gescoord. ")

elif totalScore > 7 and totalScore < 13 and ScoreO == 0 or ScoreS == 1 and totalScore > 9 : 
    print("Jij hebt VOLDOENDE gescoord.")

else :
    print("Jij hebt ONVOLDOENDE gescoord. ")