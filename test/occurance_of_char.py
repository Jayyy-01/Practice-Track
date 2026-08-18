#write a function to count the occurance of 'a' in the name "Salman"

def count_freq(name):
    count = 0
    for i in name:
        if i == 'a':
            count += 1
    print(f"Count of a is: {count}")

count_freq("salman") 