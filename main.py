# Basic Example of a Simple Python script performs mathematical operations

# Addition

def add(x, y):  # functions are defined using the def keyword x,y are the parameters
    return x + y


# Subtraction
def subtract(x, y):
    return x - y


# Multiplication
def multiply(x, y):
    return x * y


# Division
def divide(x, y):
    return x / y


###### This is the function call ######

if __name__ == "__main__":  # This is the main function
    print("Select operation.")  # This is the print statement
    print("1.Add")  # This is the print statement
    print("2.Subtract")  # This is the print statement
    print("3.Multiply")  # This is the print statement
    print("4.Divide")  # This is the print statement

    # Take input from the user
    choice = input("Enter choice(1/2/3/4):")  # This is the input statement

    num1 = int(input("Enter first number: "))  # This is the input statement
    num2 = int(input("Enter second number: "))  # This is the input statement

    if choice == '1':  # This is the if statement
        print(num1, "+", num2, "=", add(num1, num2))  # This is the print statement

    elif choice == '2':  # This is the elif statement
        print(num1, "-", num2, "=", subtract(num1, num2))  # This is the print statement

    elif choice == '3':  # This is the elif statement
        print(num1, "*", num2, "=", multiply(num1, num2))  # This is the print statement

    elif choice == '4':  # This is the elif statement
        print(num1, "/", num2, "=", divide(num1, num2))  # This is the print statement

    else:  # This is the else statement
        print("Invalid input")  # This is the print statement
