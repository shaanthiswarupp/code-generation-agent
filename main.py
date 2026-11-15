#================= Simple Calculator=============
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

#=================================

if __name__ == "__main__":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print("Addition:", add_numbers(number1, number2))
    print("Subtraction:", subtract_numbers(number1, number2))
    print("Multiplication:", multiply_numbers(number1, number2))
    print("Division:", divide_numbers(number1, number2))











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
