def mini_calculator(num1,num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    elif operation == '//':
        return num1 // num2
    else:
        return "Invalid operation"


print(mini_calculator(10,20,'+')) 
print(mini_calculator(100,55,'-'))   