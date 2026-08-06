number = int(input())

sum_of_digits = 0

while number > 0:
    temp = number % 10
    sum_of_digits = sum_of_digits + temp
    number = number // 10

print(f"Sum of Digits: {sum_of_digits}")