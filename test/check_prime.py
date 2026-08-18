#write a function to check prime number, return True if its a prime number and return False if not
#eg: 2 is prime, 9 is not prime
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
print(check_prime(13))



#better
# def check_prime(num):
#     for i in range(2,int(num**0.5)+1):
#         if i % num == 0:
#             return False
#             break
#     return True

# print(check_prime(2)) 
# print(check_prime(9))   
