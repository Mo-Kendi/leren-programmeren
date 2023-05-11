import math #omdat ik een berekening doe in de code
EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    count = 0
    for x in text:
        if x in ALLOWED_IN_WORD:
            count+=1
    return count

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    einde_zin = [".", "!","?"]
    zinnen = 0
    for x in text:
        if x in einde_zin:
            zinnen+=1
    return zinnen
# opdracht 3
def getNumberOfWords(text: str) -> int:
    return len(text.split())
# opdracht 5
def getAVIscore(text: str) -> int:
    zinnen = getNumberOfSentences(text)
    woorden = getNumberOfWords(text)
    
    gawpz = math.floor (zinnen/woorden) #rond alles af op een geheeld getal naar beneden!!
    if gawpz <=7:
        AVIscore = 5
    elif gawpz <=8:
        AVIscore = 6
    elif gawpz <=9:
        AVIscore = 7
    elif gawpz <=10:
        AVIscore = 8
    elif gawpz <=11:
        AVIscore = 11
    elif gawpz > 11:
        AVIscore = 12
    return AVIscore

