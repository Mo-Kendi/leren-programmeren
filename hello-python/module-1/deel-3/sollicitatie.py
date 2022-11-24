print('sollicitatie')
ervaring = int(input("Hoeveel jaar heeft u evaring met dieren-dressuur?"))
if ervaring <= 4:
    ervaring2 = int(input("Hoeveel jaar heeft u ervaring met jongeleren?"))
    if ervaring2 <= 5:
        ervaring3 = int(input("Hoeveel jaar ervaring heeft u met de acrobatiek?"))
        ###############################################

name = input("Wat is uw naam?")
if name == 'slemmer':
    raise NameError ('slemmer u mag sws niet solliciteren helaas pinda kaas')
diploma = input("Heeft u een MBO-4 diploma ondernemen? (ja/nee)")
if diploma == 'nee':
    raise NameError ('ben je zo ver nog dat je geen mbo diploma hebt????')
bewijs = input("Heeft u een vrachtwagen rjibewijs? (ja/nee)")
if bewijs == 'nee':
    raise NameError ('nou nou zelfs mijn opa heeft dat')
hoed = input("Heeft u een hoge hoed? (ja/nee)")
man = input("Bent u een man? (ja/nee)")


if man == "ja":
    snor = input('heeft u een snor? (ja/nee)') 
    
    if snor == "ja":
        snor = int(input('hoe lang is uw snor? (cm)'))

else:
    haar = input("Is uw haar rood en krullig(ja/nee)")
    haar2 = int(input("Hoe lang is uw haar?(cm)"))

lengte = int(input("Hoe lang bent u? (cm)"))
gewicht = int(input("Hoe zwaar bent u? (kg)"))
certificaat = input(
    "Heeft u het certificaat, 'overleven met gevaarlijk personeel'? (ja/nee)")

####################
#eigen vragen
huisdieren = input('houdt u van huisdieren? (ja/nee)')
zwemmen = int(input('hoe vaak zwemt u per week? '))
stinkkaas = input('stinkt u naar kaas? (ja/nee)')
naarHuis = input('wilt u naar huis? (ja/nee)')
#######################

totaleScore = 0
if ervaring > 4:
    totaleScore += 1

if ervaring <= 4:
    if ervaring2 > 5:
        totaleScore += 1
if ervaring <= 4:
    if ervaring2 <= 5:
        if ervaring3 > 3:
            totaleScore += 1

if diploma == "ja":
    totaleScore += 1

if bewijs == "ja":
    totaleScore += 1

if hoed == "ja":
    totaleScore += 1

if man == "ja":
    if snor > 10:
        totaleScore += 1

if man == "nee":
    if haar == "ja":
        totaleScore += 1

    if haar2 > 20:
        totaleScore += 1

if lengte > 150:
    totaleScore += 1

if gewicht > 90:
    totaleScore += 1

if certificaat == "ja":
    totaleScore += 1

if man == "ja":
    if totaleScore >= 8:
        print("U mag gaan soliciteren!")
    else:
        print("U mag helaas niet gaan soliciteren!")

else:
    if totaleScore >= 9:
        print("U mag gaan soliciteren!")

    else:
        print("U mag helaas niet soliciteren")
