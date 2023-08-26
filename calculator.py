# Define calculation functions
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"


# Define the operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Calculator loop
calculator_on = True
while calculator_on:
    a = float(input("Enter the first number: "))

    print("Enter the operation:")
    for operation in operations:
        print(operation)

    done_calculating = False
    while not done_calculating:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol in operations:
            b = float(input("Enter the next number: "))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(a, b)
            print(f"{a} {operation_symbol} {b} = {answer}")

            should_continue = input("Enter 'y' to continue with the result, "
                                    "'n' to start a new calculation, "
                                    "or 'q' to quit: ").lower()

            if should_continue == "y":
                a = answer
            elif should_continue == "n":
                done_calculating = True
            elif should_continue == "q":
                print("Closing the calculator!")
                done_calculating = True
                calculator_on = False
            else:
                print("Invalid choice!\nRestarting.")
                done_calculating = True
        else:
            print("Invalid operation symbol. Please choose from the available operations.")
