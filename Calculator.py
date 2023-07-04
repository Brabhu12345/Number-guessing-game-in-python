#hi
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multi(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
name = input("pls enter your name: ")
print("hi " + name)
print("welcome to python calculator!!")
print("select your operator:")
print("(1) add")
print("(2) sub")
print("(3) multi")
print("(4) div")
op = int(input())
if op == 1:
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    print("result: " + str(add(num1, num2)))
elif op == 2:
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    print("result: " + str(sub(num1, num2)))
elif op == 3:
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    print("result: " + str(multi(num1, num2)))

elif op == 4:
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    print("result: " + str(div(num1, num2)))
else:
    print("invalid input!!")
    print("try again!!")
