student_count = int(input())
marks = []

for i in range(student_count):
    num = int(input())
    marks.append(num)

position = int(input())
corrected_number = int(input())
passing_mark = int(input())

marks[position - 1] = corrected_number

highest = marks[0]
lowest = marks[0]
total = 0
count = 0

for i in marks:
    total += i
    count += 1
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

passed_students = 0
for i in marks:
    if i >= passing_mark:
        passed_students += 1

average = total / count
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Passed Students: {passed_students}")