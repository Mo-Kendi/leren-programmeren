x = 0
while True:
    vraag = input('schrijf quit?')
    if vraag == 'quit':
        print(x)
        break
    else:
        print('probeer opnieuw')
        x+=1