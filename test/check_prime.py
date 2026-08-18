def check_prime(num):
    if num < 2:
        return False
    elif num >2:
        for i in range(2,num):
            if i % num == 0:
                return False
                break
        return True
    return False

print(check_prime(2))
print(check_prime(9)) 