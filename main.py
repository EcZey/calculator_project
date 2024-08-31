import os
from art import logo


def clear_terminal():
    _ = os.system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2


def calculator():
    print(logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        num2 = float(input("What's the next number?: "))
        operation_symbol = input("Pick an operation from the above list: ")

        if operation_symbol in operations:
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("Invalid operation. Please try again.")
            continue

        continue_with_answer = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit: ").lower()

        if continue_with_answer == "y":
            num1 = answer
        else:
            should_continue = False
            clear_terminal()
            calculator()


calculator()
