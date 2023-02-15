# calculator

number1=eval(input("Enter first number"))
number2=eval(input("Enter second number"))

operator=input("Enter operator:")

def add(number1,number2):
    result=number1 + number2
    return result

def subtract(number1,number2):
    result = number1 - number2
    return result

def divide(number1,number2):
    result=(number1/number2)
    return result

def multiply(number1,number2):
    result=(number1*number2)
    return result

