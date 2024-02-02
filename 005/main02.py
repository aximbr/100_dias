students_height = input("Enter list of students height separet by space: ").split()

sum_height = 0
count = 0

for n in students_height:
    sum_height += int(n)
    count += 1

average = round(sum_height/count)

print(f"The average of height is {average}")