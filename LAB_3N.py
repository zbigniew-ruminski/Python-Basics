num1 = float(input("First number: "))
op = input("Operator: ")
num2 = float(input("Second numer: "))
#
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")