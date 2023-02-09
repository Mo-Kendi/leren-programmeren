def fibonacci(minimum: int) -> str:
    num1, num2 = 0, 1   
    teller = 0
    volgorde = ""
    while teller < 100:
        if num1 > minimum:
            volgorde += (str(num1) if volgorde == "" else ", {}".format(num1))
            teller += 1
        laatste_2_nummers = num1 + num2
        num1 = num2
        num2 = laatste_2_nummers
    return volgorde


while not (amount := input("Vanaf welk nummer wilt u dat wij printen?")).isdigit():
    print("Noem een NUMMER op, bedankt.")

print(fibonacci(int(amount)))
