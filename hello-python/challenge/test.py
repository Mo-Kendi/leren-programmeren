print('if u wanna proceed in the game u need to choose a weapon')
print('sword')
print('shield')
print('dagger')
sword = 'sword'
shield = 'shield'
dagger = 'dagger'
weapon = input('wich one do u choose? ')

if  weapon in ["sword"]:
    sword = input(f'are you sure u want to choose {sword} ')
elif weapon in ['shield']:
    shield = input('shield is trash u will die')
elif weapon in ['dagger']:
    dagger = input('wise choice')
else:
    print('thats not mentioned')

