from spel_tekens import *

def welcome():
    print('Welcome to Dino game!')
    story = 0
    while story == 0:
        age = input('Are you old enough (18) to play? (yes/no) ')
        if age.lower() == 'no':
            print('Then what are you doing here? Try again when you are old enough.')
            exit()
        elif age.lower() == 'yes':
            print('You are good to go!')
            story += 1
        else:
            print('Please enter "yes" or "no".')
    return story

def choose_weapon():
    print('This story contains several bosses. To end the game, you need to walk through the story, kill the minions, and level up!')
    print('If you want to proceed in the game, you need to choose a weapon:')
    print('sword')
    print('shield')
    print('dagger')
    weapon = 'none'
    while weapon not in ['sword', 'shield', 'dagger']:
        weapon = input('Which one do you choose? ')
        if weapon == 'sword':
            print(f'Oeeehhh sword! Let them fear the true samurai inside you!')
        elif weapon == 'shield':
            print('Shield is trash. You will die.')
        elif weapon == 'dagger':
            print('Wise choice!')
        else:
            print('That\'s not mentioned.')
    return weapon

def ready_to_fight():
    while True:
        begin = input('Now you can begin fighting. This is a miniboss. Do you want to proceed? (yes/no) ')
        if begin.lower() == 'no':
            print('Try again when you are ready: BE A MAN!')
            exit()
        elif begin.lower() == 'yes':
            print('May the gods protect you!')
            print('\n')
            return False
        else:
            print('Please enter "yes" or "no".')

def first_fight(weapon):
    print(DINO1)
    attack = True
    result = 0
    while attack == True:
        attack = input('Press "e" to attack!')
        if attack.lower() == 'e':
            if weapon != "sword":
                print("you cant defeat him with your weapon")
            else:
                print('What a hit! Nice job! You will proceed to the next level.')
                print('\n')
        elif weapon == "sword":
            result += 1
        else:
            attack = False
            result = 0
    # return attack
    return result

def second_fight():
    story = 1
    while story < 3:
        way = input('''Now you are at a crossway. You have to choose to go left or right!
        Where do you want to go? Choose a direction! But you know there are consequences for which way you choose... ''')
        if way.lower() == 'left':
            print('You are now in the jungle. Here you will play against the pro old sexy trex king. This king is not easy; you will struggle!')
            ready = input('Are you ready? (yes/no) ')
            if ready.lower() == 'yes':
                print('Let the game begin!')
                story += 1
            elif ready.lower() == 'no':
                print('Yeah, no problem. You will get over it. Just run!')
            else:
                print('Please enter "yes" or "no".')
            print(DINO2)
            attack1 = input('Press "s" to attack!')
            if attack1.lower() == 's':
                print("That was a good hit! Let's go!")
            else:    
                print(GAME_OVER)
        elif way.lower() == 'right':
                print('you are right, right is the right answer nou you can skip miniboss to go to the last boss!')
                story+=1
                print(DINO3)
                skip = input('press x to skip')
                if skip == "x":
                    print('Now you are in the last fase, you have to defeat the last boss to win the game!')
        else:
            print('thats not a direction')    
    print('\n')
    return way

#last boss
def last_boss():
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
    return lastFase