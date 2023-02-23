def optellen(nummer1, nummer2):
    return nummer1 + nummer2


def aftrekken(nummer1, nummer2):
    return nummer1 - nummer2


def keer(nummer1, nummer2):
    return nummer1 * nummer2


def delen(nummer1, nummer2):
    return nummer1 / nummer2


sommen = {
    'a': optellen, #plus
    'b': aftrekken, #min
    'c': keer, #vermenigvuldigen
    'd': delen, #delen
    'e': optellen,  # ophogen
    'f': aftrekken,  # verlagen
    'g': keer,  # verdubblen
    'h': delen,  # halveren
}


def get_number(prompt):
    while True:
            return float(input(prompt))


result = None
eerste_ronde = True
num1 = False
num2 = False
while True:
    if eerste_ronde == True:
        som = input("wat wil je doen?\n (a)optellen\n (b)aftrekken\n (c)vermenigvuldigen\n (d)delen\n (e)optellen de nummer\n (f)aftrekken de nummer\n (g)vermenigvuldigen de nummer\n (h)delen door\n (q)uit\n").lower()
    else:
        som = input(f"wat wil je doen met {result} ?\n (a)optellen\n (b)aftrekken\n (c)vermenigvuldigen\n (d)delen\n (e)optellen de nummer\n (f)aftrekke de nummer\n (g)vermenigvuldigen de nummer\n (h)delen door\n (q)uit\n").lower()
    if som == 'q':
        print(num1)
        break
    elif som in sommen:
        if num1 == False:
            num1 = get_number("vul de eerste nummer: ")
        
        if som == 'e':
            num2 = 1
        elif som == 'f':
            num2 = 1
        elif som == 'g':
            num2 = 2
        elif som == 'h':
            num2 = 2
        if num2 == False:
            num2 = get_number("vul de tweede nummer: ")
        #print(num1 , num2)    
        result = sommen[som](num1, num2)
        print(f"het resultaat is: {result}")
        num1 = result
        eerste_ronde = False
        num2= False
    else:
        print("verkeerde antwoord, voer een geldig getal in")