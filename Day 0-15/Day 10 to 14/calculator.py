def add(n1, n2):
    return n1 + n2
def substract(n1 ,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def calculator():
    operation = {"+":add,
                "-":substract,
                "*":multiply,
                "/":divide
                }
    rep = True
    num1 = float(input("what is ur first number ?\n"))

    for i in operation:
        print(i)



    while rep :

        operation_symbol = input("pick an operation from the line above\n")
        num2 = float(input("what is ur next number ?\n"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        x =input("do u want to continue if u want type 'y' if not type 'n' ").lower()
        if x == "y":
            num1 = answer
        else :
            rep = False
            calculator()
calculator()
