from art import logo

def add(n1, n2):
    """
    Returns the sum of n1 and n2.
    
    :param n1: The first number to add.
    :param n2: The second number to add.
    :return: The sum of n1 and n2.
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Returns the difference of n1 and n2.
    
    :param n1: The minuend.
    :param n2: The subtrahend.
    :return: The difference of n1 and n2.
    """
    return n1 - n2

def multipy(n1, n2):
    """
    Returns the product of n1 and n2.
    
    :param n1: The first number to multiply.
    :param n2: The second number to multiply.
    :return: The product of n1 and n2.
    """
    return n1 * n2

def divide(n1, n2):
    """
    Returns the quotient of n1 and n2.
    
    :param n1: The dividend.
    :param n2: The divisor.
    :return: The quotient of n1 and n2.
    """
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multipy,
    "/": divide,
}

def calculator():
    """
    This function implements a command line calculator. It first prints the logo then
    enters a loop where it asks for a number and an operation. It then prints the result
    of the operation and asks if the user wants to continue calculating with that
    number or start with a new number. If the user chooses to continue with that number,
    the loop continues. If the user chooses to start with a new number, the function calls
    itself and the loop starts again. If the user chooses to quit, the loop ends and the
    function returns.
    """
    print(logo)
    calculator_on = True
    number_1 = float(input("Enter the first number: "))
    while calculator_on:
        for keys in functions:
            print(keys)
        operation = input("Pick an operation: ")
        number_2 = float(input("Enter the second number: "))
        result = functions[operation](number_1, number_2)
        print(f"{number_1} {operation} {number_2} = {result}")

        choice = input(f"To continue calculating with {result} press 'y' or to continue with a new number press 'n' or 'q' to quit \n").lower()

        if choice == "y":
            number_1 = result
        elif choice == "n":
            calculator_on = False
            print("\n" * 20)
            calculator()
        else:
            calculator_on = False

calculator()


