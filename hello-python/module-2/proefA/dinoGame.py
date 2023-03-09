from spel_tekens import *
from functions import *

story = welcome()  
weapon = choose_weapon() 
begin = ready_to_fight()
attack = first_fight()

print('\n')

while story == 3:
        way = input('''now you are in crossway, you have to choos to go left or right!
        Where do you want to go? choose a direction! but u know there are consequences wich way you choose---___--- ''')
        if way == 'left':
            print('you are now in the jungle here you will play against the pro old sexy trex king. this king is not ez, you will struggle!')
            ready = input('are you ready? yes/no')
            if ready == 'yes':
                print('let the game begin')
                story+=1
            elif ready == 'no':
                print('yea no problem you will get over it just run!')
            else:
                print('thats is not asked! try again ')
            print(DINO2)
            attack1 = input('press s to attack!')
            if attack1 == "s":
                print("that was a good hit, lesgoooo")
            else :    
                print(GAME_OVER)
        elif way == 'right':
            print('you are right, right is the right answer nou you can skip miniboss to go to the last boss!')
            story+=1
            print(DINO3)
            skip = input('press x to skip')
            if skip == "x":
                print('Now you are in the last fase, you have to defeat the last boss to win the game!')
        else:
            print('thats not a direction')

        
print('\n')



#last boss
lastFase = input('Hello mighty dino slayer, this is the last fase, now u will fase the true fear! press x to enter the room')
if lastFase =="x":
    print(BOSS)
    attack2 = input('this is the true fear! press a to attack!')
    if attack2 == 'a':
        attack3 = input('hit him again!')
        attack4 = input('once again!')
        if attack4 == 'a':
            print(BADGE)    
        else :
            print(GAME_OVER)
else :
    print(GAME_OVER)