dag = input('Welke dag is het?')

week = [ 'maandag', 'dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
x = 3
while True:
    print(week[x])
    if week[x] == dag: #expression uit komst boolien
        break
    x += 1