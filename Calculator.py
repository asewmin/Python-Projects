print("*** Welcome to the Calculator ***\n")


x = float(input(" Enter the first number: "))
operator = input("Enter operator (+, -, *, /):" )
y = float(input("Enter the second number: "))

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def divide(x, y):
    if y == 0:  
        return "Division by zero is not possible"
    else:
        return x / y

def multiplication(x,y):
    return x * y

if operator == "+":
    result = add(x, y)

elif operator == "-":
    result = substract(x, y)

elif operator == "/":
    result = divide(x, y)

elif operator == "*":
    result = multiplication(x, y)

else:
    result = "Invalid operator"

print("Result =", result)




