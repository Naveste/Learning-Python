# Calculator

# add
def add(n1, n2):
    return n1 + n2

#subtract
def sub(n1, n2):
    return n1 - n2

#multiply
def multi(n1, n2):
    return n1 * n2

#divide
def div(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': div,
}

def calc():
    num1 = float(input("What's the first number?"))
    for operator in operations:
        print(operator)
    active = True

    while active:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input(("What's the next number?")))

        if operation_symbol == '+':
            answer = add(num1, num2)
        elif operation_symbol == '-':
            answer = sub(num1, num2)
        elif operation_symbol == '*':
            answer = multi(num1, num2)
        elif operation_symbol == '/':
            answer = div(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        proceed = input(f"Type 'y' to continue to calculating with {answer}, or type 'n' to start a new calculation, or 'exit' to exit.: ")
        if proceed == 'y':
            num1 = answer
        elif proceed == 'n':
            active = False
            calc()
        else:
            active = False
calc()