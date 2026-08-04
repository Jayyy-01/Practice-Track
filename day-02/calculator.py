a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
op = input("enter the operation to be performed (+,-,*,/,//): ")
if op == "+":
    print(f"Sum of a and b is {a+b}")
elif op == "-":
    print(f"Subtraction of a and b is {a-b}")
elif op == "*":
    print(f"Multiplication of a and b is {a*b}")
elif op == "/":
    print(f"Division of a and b is {a/b}")
elif op == "//":
    print(f"Floor Division of a and b is {a//b}")
else:
    print("Invalid operator")