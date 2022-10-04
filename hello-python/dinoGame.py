


from asyncore import read
from tkinter.messagebox import YES
from turtle import left


print('welcome to dino game')
age = input('are you old enough to play? (yes/no) ')
if age == 'no':
    print('then what are you doing here? what ever')

print('this story contains several bosses. to end the game you need to walk through the story and kill the minions and level up!')

print('if u wanna proceed in the game u need to choose a weapon:')
print('sword')
print('shield')
print('dagger')
sword = 'sword'
shield = 'shield'
dagger = 'dagger'
weapon = input('wich one do u choose? ')

if  weapon in ["sword"]:
    sword = input(f'are you sure u want to choose {sword} (yes/no) ')
elif weapon in ['shield']:
    shield = print('shield is trash u will die')
elif weapon in ['dagger']:
    dagger = print('wise choice')
else:
    print('thats not mentioned')

print('\n')
##########################
begin = input('now you can begin fighting, this is a miniboss, do you want to proceed? (yes/no) ')
if begin == 'no':
    print('this one is ez u should be save!')
elif begin == 'yes':
    print('may the gods protect you')
else :
    print('Wrong answer buddy')
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

attack = input('press e to attack!')
if attack == 'e':
    print('nice job, you will proceed to the next level')
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


print('\n')

way = input('''now you are in crossway, you have to choos to go left or right!
Where do you want to go? choose a direction! but u know there are consciences wich way you choose---___--- ''')
if way == 'left':
    print('you are now in the jungle here you will play against the pro old sexy trex king. this king is not ez, you will struggle!')
    ready = input('are you ready? yes/no')
    if ready == 'yes':
        print('let the game begin')
    elif ready == 'no':
        print('yea no problem you will get over it just run!')
    else:
        print('thats is not asked?')
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




elif way == 'right':
    print('you are right, right is the right answer nou you can skip miniboss to go to the last boss!')
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

