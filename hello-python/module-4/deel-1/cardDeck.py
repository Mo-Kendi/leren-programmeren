import random
kaarten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas")
Kleur = ("harten ","klaveren ","schoppen ","ruiten ")
jokers = ("Joker1","Joker2")
deck = []
for inhoud in Kleur[0:4]:
    for inhoud2 in kaarten[0:12]:
        deck.append (inhoud + inhoud2)
deck.append ("Joker1")
deck.append ("Joker2")
random.shuffle(deck)
for y in range(7):
    print(f"Karten {y+1} : {deck[0]}") #straat met huis nummer//### list net als huizen
    deck.pop(0)
print(deck)


#   __ dit heet snake case####