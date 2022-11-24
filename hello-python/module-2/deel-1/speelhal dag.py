

from email import message


mensen = int(input('met hoeveel mesnen ga je? '))
################################################
ticketpijs = 7.45
tickets = mensen * ticketpijs
tickets_af = round(tickets,0)
##################################################
minuten = int(input('aantal minuten?  '))
vr = 0.37 / 5
vrprijs = minuten * vr
vr_af = round (tickets,0)
###################################################
print('ticket totaal prijs', tickets_af) 
print('vr totaal prijs', vr_af)
##################################################
eindprijs = tickets + vr_af
eindprijs_cent = eindprijs * 100

print(
    f"dagje-uit met {mensen} mensen in de Speelhal met {minuten} minuten VR kost je : {eindprijs_cent} cent")
""