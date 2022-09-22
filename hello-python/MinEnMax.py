a = int(input("Wat is a?"))
b = int(input("Wat is b?"))

if a > b:
    Max = a
    Min = b
    print("het grootste getal is a met de waarde van", Max)

elif a < b:
    Min = a
    Max = b
    print('a is het kleinste getal met de waarde van', Min)

else:
    #a == b dit kan ook zonder dit
    Min = a
    Max = a
    print("a en b zijn even groot!")


print(f'het minimum is {Min} en het maximum is {Max}')
