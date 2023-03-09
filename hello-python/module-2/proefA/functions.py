from spel_tekens import *
def welcome():
    print('welcome to dino game')
    story = 0
    while story == 0:
            age = input('are you old enough (18) to play? (yes/no) ')
            if age == 'no':
                print('then what are you doing here? try again when u are old enough')
                exit()
            elif age == 'yes':
                print('ur good to go')
                story+=1
            else :
                print('try again!')
    return story

#################### 
def choose_weapon():
    print('this story contains several bosses. to end the game you need to walk through the story and kill the minions and level up!')
    print('if u wanna proceed in the game u need to choose a weapon:')
    print('sword')
    print('shield')
    print('dagger')
    weapon = 'none'
    while not weapon in ['sword','shield','dagger']:
            weapon = input('wich one do u choose? ')
            if  weapon in ["sword"]:
                print(f'oeeehhh sword let them fear the true samurai inside u ')
            elif weapon in ['shield']:
                print('shield is trash u will die')
            elif weapon in ['dagger']:
                print('wise choice')
            else:
                print('thats not mentioned')
    return weapon

##########################
def ready_to_fight():
    begin = True
    while begin == True:
            begin = input('now you can begin fighting, this is a miniboss, do you want to proceed? (yes/no) ')
            if begin == 'no':
                print('try again when ur ready: BE A MAN')
                begin == False
                exit()
            elif begin == 'yes':
                print('may the gods protect you')
                begin == True
                print('\n')
            else :
                print('Wrong answer buddy')

            return begin
##########################
def first_fight():
    print(DINO1)
    attack == True
    while attack == True:
            attack = input('press e to attack!')
            if attack == 'e':
                print('what a hit! nice job, you will proceed to the next level')
            else:
                attack == False
                print(GAME_OVER)
    return attack