from spel_tekens import *
from functions import *

story = welcome()  
weapon = choose_weapon() 
begin = ready_to_fight()
result = first_fight(weapon)
if result == 0:
    print(GAME_OVER)
    exit()
way = second_fight()
lastFase = last_boss()