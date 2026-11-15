# Simple Calculator
def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
# Main program
if __name__ == "__main__":
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == "1":
            result = add_numbers(number1, number2)
        elif choice == "2":
            result = subtract_numbers(number1, number2)
        elif choice == "3":
            result = multiply_numbers(number1, number2)
        elif choice == "4":
            result = divide_numbers(number1, number2)
        print("Result:", result)










# #================= Simple Calculator=============
# def add_numbers(a, b):
#     return a + b
# def subtract_numbers(a, b):
#     return a - b
# def multiply_numbers(a, b):
#     return a * b
# def divide_numbers(a, b):
#     if b == 0:
#         return "Error: Cannot divide by zero"
#     return a / b

# #=================================

# if __name__ == "__main__":
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))
#     print("Addition:", add_numbers(number1, number2))
#     print("Subtraction:", subtract_numbers(number1, number2))
#     print("Multiplication:", multiply_numbers(number1, number2))
#     print("Division:", divide_numbers(number1, number2))











# # Simple Calculator
# def add_numbers(a, b):
#     return a + b


# if __name__ == "__main__":
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     result = add_numbers(number1, number2)

#     print("Addition result:", result)




# My first interactive Python program

# def greet_user(name):
#     return f"Hello, {name}! Welcome to Code Generation Agent."

# if __name__ == "__main__":
#     user_name = input("Enter your name: ")
#     message = greet_user(user_name)
#     print(message)







# # My first Python program

# def greet_user(name):
#     return f"Hello, {name}! Welcome to Code Generation Agent."

# if __name__ == "__main__":
#     #message = greet_user("Developer")
#     message = greet_user("Shaanthi")
#     print(message)
