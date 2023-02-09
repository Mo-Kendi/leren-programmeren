def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


operations = {
    'a': addition, #plus
    'b': subtraction, #min
    'c': multiplication, #vermenigvuldigen
    'd': division, #delen
    'e': addition,  # ophogen
    'f': subtraction,  # verlagen
    'g': multiplication,  # verdubblen
    'h': division,  # halveren
}


def get_number(prompt):
    while True:
            return float(input(prompt))


result = None
firsturn = True
num1 = False
num2 = False
while True:
    if firsturn == True:
        operation = input("What would you like to do?\n (a)add\n (b)subtract\n (c)multiply\n (d)divide\n (e)addition the number\n (f)subtraction the number\n (g)multiplication the number\n (h)division the number\n (q)uit\n").lower()
    else:
        operation = input(f"What would you like to do with {result} ?\n (a)add\n (b)subtract\n (c)multiply\n (d)divide\n (e)addition the number\n (f)subtraction the number\n (g)multiplication the number\n (h)division the number\n (q)uit\n").lower()
    if operation == 'q':
        print(num1)
        break
    elif operation in operations:
        if num1 == False:
            num1 = get_number("Enter the first number: ")
        
        if operation == 'e':
            num2 = 1
        elif operation == 'f':
            num2 = 1
        elif operation == 'g':
            num2 = 2
        elif operation == 'h':
            num2 = 2
        if num2 == False:
            num2 = get_number("Enter the second number: ")
        print(num1 , num2)    
        result = operations[operation](num1, num2)
        print(f"The result is: {result}")
        num1 = result
        firsturn = False
        num2= False
    else:
        print("Invalid operation. Please choose a valid option.")