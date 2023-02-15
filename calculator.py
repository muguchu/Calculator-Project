# calculator

number1=eval(input("Enter first number"))
number2=eval(input("Enter second number"))

operator=input("Enter operator:")

def add(number1,number2):
    result=number1 + number2
    print(result)

def subtract(number1,number2):
    result = number1 - number2
    print(result)

def divide(number1,number2):
    result=(number1/number2)
    print(result)


def multiply(number1,number2):
    result=(number1*number2)
    print(result)

if operator=="+":
    add(number1,number2)
elif operator=="-":
    subtract(number1,number2)
elif operator=="/":
    divide(number1,number2)
elif operator=="*" or operator=="X" or operator=="x":
    multiply(number1,number2)
else:
    print("Invalid operator")
    
