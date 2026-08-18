#write a function which tells the occurance of target character in a string and it shld accept str and target char as argument
# eg: str = "salman" , target = 'a' and it should print the occurance of 'a' in "salman"
def count_freq(str,target):
    count = 0
    for ch in str:
        if ch == target:
            count += 1
    print(f"Count of {target} is: {count}")

count_freq("salman","a")  
count_freq("jayasree",'a')