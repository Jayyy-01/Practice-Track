#Write a function to print even numbers from 1 to 100

def even_numbers():
    for i in range(1,101):
        if i % 2 == 0:
            print(i,end=" ")
even_numbers() 