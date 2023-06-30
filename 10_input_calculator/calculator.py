print("CALCULATOR")


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/ n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide

}

def calculator():
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    continue_ = True
    while continue_:
        operation_symbol = input("Pick an operation from the lines above: ")
        num2 = float(input("What is the next number? "))
        function = operations[operation_symbol]
        answer = function(num1,num2)


        print(f'{num1} {operation_symbol} {num2} = {answer}')

        continue_value = input("Type 'y' to continue or 'n' to start a new calculation: ")
        if continue_value == 'y':
            num1 = answer
        else:
            continue_ = False
            calculator()

calculator()