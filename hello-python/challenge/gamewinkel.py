# een spelletje kost in de winkle 24,95, maar gamewinkels krijgen 40 procent korting bij inkoop
# Het versturen vanuit de leverancier kost 1,00 voor het eerste spel, en 25 cent voor iedere volgende game. Bereken hoeveel de gamewinkel betaald voor 60 spelletjes

spel_prijs = 24.95
korting = 0.4

verzendkosten_eerste = 1.00
verzendkosten_volgende = 0.25

aantal_spellen = 60

prijs_voor_korting = spel_prijs * aantal_spellen
prijs_met_korting = prijs_voor_korting * (1 - korting)
verzendkosten = verzendkosten_eerste + verzendkosten_volgende * (aantal_spellen - 1)
totaal_prijs = prijs_met_korting + verzendkosten

print(f"De gamewinkel betaalt {round(totaal_prijs, 2)} voor 60 spellen.")

# SPEL_PRIJS = 24.95
# KROTING = 0.4
# def game (aantal):
