dag = input('Welke dag is het?')

week = [ 'maandag', 'dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
x = 0
while True:
    print(week[x])
    if week[x] == dag:
        break
    x += 1