from operator import truediv


print('welcome to dino game')
story = 0
while story == 0:
    while True:
        age = input('are you old enough (18) to play? (yes/no) ')
        if age == 'no':
            print('then what are you doing here? try again when u are old enough')
            exit()
        elif age == 'yes':
            print('ur good to go')
            story+=1
        else :
            print('try again!')
        break
    

print('this story contains several bosses. to end the game you need to walk through the story and kill the minions and level up!')

print('if u wanna proceed in the game u need to choose a weapon:')
print('sword')
print('shield')
print('dagger')
sword = 'sword'
sword1 = False
shield = 'shield'
shield1 = False
dagger = 'dagger'
dagger1 = False

while story == 1:
    while True:
        weapon = input('wich one do u choose? ')

        if  weapon in ["sword"]:
            sword = print(f'oeeehhh sword let them fear the true samurai inside u ')
            sword1 = True
            story+=1
        elif weapon in ['shield']:
            shield = print('shield is trash u will die')
            shield1 = True
            story+=1
        elif weapon in ['dagger']:
            dagger = print('wise choice')
            dagger1 = True
            story+=1
        else:
            print('thats not mentioned')
        break

print('\n')
##########################
while story == 2:
    while True:
        begin = input('now you can begin fighting, this is a miniboss, do you want to proceed? (yes/no) ')
        if begin == 'no':
            print('try again when ur ready: BE A MAN')
            exit()
        elif begin == 'yes':
            print('may the gods protect you')
            story+=1
        else :
            print('Wrong answer buddy')
        break
##########################

print('''
                     /~~~~~~~~~~~~\_
 _+=+_             _[~  /~~~~~~~~~~~~\_
{""|""}         [~~~    [~   /~~~~~~~~~\_
 """:-'~[~[~"~[~  ((++     [~  _/~~~~~~~~\_
      '=_   [    ,==, ((++    [    /~~~~~~~\-~~~-.
         ~-_ _=+-(   )/   ((++  .~~~.[~~~~(  {@} \`.
                 /   }\ /     (     }     (   .   ''}
                (  .+   \ /  //     )    / .,  """"/
                \\  \     \ (   .+~~\_  /.= /'""""
                <"_V_">      \\  \    ~~~~~~\\  \
                              \\  \          \\  \
                              <"_V_">        <"_V_">
''')
while story == 3:
    while True :
        attack = input('press e to attack!')
        if attack == 'e':
            print('what a hit! nice job, you will proceed to the next level')
            story+=1
        else:
            print('''
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        you are trsah, you cant even press e. kleine speler
        ''')
            exit()
        break

print('\n')

while story == 4:
    while True :
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
            print('''                                                     -- __
                                                          ~ (@)  ~~~---_
                                                        {     `-_~=======)
                                                        {    (_  ',
                                                         ~    . = _',
                                                          ~    '.  =-'
                                                            ~     :
        .                                                -~     ("");
         '.                                         --~        \  \ ;
           ".-_                                   -~            \  \;      _-====
              -~- _                          -~                 {  "---- _'-====
                ~- _~-  _              _ -~                     ~---------==.=`
                     ~-  ~~-----~~~~~~       .+++~~~~~~~~-__   /
                         ~-   __            {   -     +   }   /
                                  ~- ______{_    _ -=\ / /_ ~
                                      :      ~--~    // /         ..-
                                      :   / /      // /         ((
                                      :  / /      {   `-------=. ))
                                      :   /        '"=--------. }o
                         .=._________,'  )                     ))
                         )  _________ -''                     ~~
                        / /  _ _                   =
                       (_.-.'O'-'. ''')
            attack1 = input('press s to attack!')
            if attack1 == "s":
                print("that was a good hit, lesgoooo")
            else :    
                print('''that was not the right key-_- 
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ''')
        elif way == 'right':
            print('you are right, right is the right answer nou you can skip miniboss to go to the last boss!')
            story+=1
            print('''                         . - ~ ~ ~ - .
              ..     _      .-~               ~-.
             //|     \ `..~                      `.
            || |      }  }              /       \  \
        (\   \\ \~^..'                 |         }  \
         \`.-~  o      /       }       |        /    \
         (__          |       /        |       /      `.
          `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.
                      |     /          |     /     ~-.     ~- _
                      |_____|          |_____|         ~ - . _ _~_-_''')
            skip = input('press x to skip')
            if skip == "x":
                print('Now you are in the last fase, you have to defeat the last boss to win the game!')
        else:
            print('thats not a direction')
        break
        
print('\n')



#last boss
lastFase = input('Hello mighty dino slayer, this is the last fase, now u will fase the true fear! press x to enter the room')
if lastFase =="x":
    print('''  __
              / _)
     _.----._/ /
    /         /
 __/ (  | (  |
/__.-'|_|--|_| ''')
    attack2 = input('this is the true fear! press a to attack!')
    if attack2 == 'a':
        attack3 = input('hit him again!')
        attack4 = input('once again!')
        if attack4 == 'a':
            print('''well played! this is your dinoslayer badge!                       _..----------.._                       
                  .-=""        _       ""=-.                  
               .-"    _.--""j _\""""--._    "-.               
            .-"  .-i   \   / / \;       ""--.  "-.            
          .'  .-"  : ( "  : :                "-.  `.          
        .'  .'      `.`.   \ \                  `.  `.        
       /  .'      .---" ""--`."-./'---.           `.  \       
      /  /      .'                    '-.           \  \      
     /  /      /                         `.          \  \     
    /  /      /                  ,--._   (            \  \    
   ,  /    '-')                  `---'    `.           \  .   
  .  :      .'                              "-._.-.     ;  ,  
  ;  ;     /            :;         ,-"-.    ,--.   )    :  :  
 :  :     :             ::        :_    "-. '-'   `,     ;  ; 
 |  |     :              \\     .--."-.    `._ _   ;     |  | 
 ;  ;     :              / "---"    "-."-.    l.`./      :  : 
:  :      ;             :              `. "-._; \         ;  ;
;  ;      ;             ;                `..___/\\        :  :
;  ;      ;             :                        \\    _  :  :
:  :     /              '.                        ;;.__)) ;  ;
 ;  ; .-'                 "-...______...--._      ::`--' :  : 
 |  |  `--'\                                "-.    \`._, |  | 
 :  :       \                                  `.   "-"  ;  ; 
  ;  ;       `.                                  \      :   ' 
  '  :        ;                                   ;     ;  '  
   '  \    _  : :`.                               :    /  /   
    \  \   \`-' ; ; ._                             ;  /  /    
     \  \   `--'  : ; "-.                          : /  /     
      \  \        ;/     \                         ;/  /      
       \  `.              ;                        '  /       
        `.  "-.   bug    /                          .'        
          `.   "-..__..-"                         .'          
            "-.                                .-"            
               "-._                        _.-"               
                   """---...______...---"""  
                   I hope u have enjoyed playing this game!
                   made by Mo kendi''')    
        else :
            print(''' u had to press a
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
you are trsah, you cant even press d. kleine speler
 ''')
else :
    print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
you are trsah, you cant even press a. kleine speler
''')