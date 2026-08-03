number = int(input("enter the number: "))
if number < 2:
    print("Not a prime number")
else:
    for i in range(2,number):
        if number % i == 0:
            print(f'{number} is not a prime number')
            break
    else:
        print(f'{number} is a prime number')