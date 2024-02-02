#Obtain the highest score
students_score = input("Enter list of score for students separet by space: ").split()

#convert to int
for n in range (0, len(students_score)):
    students_score[n] = int(students_score[n])
#end of for
    
high_score = 0

for score in students_score:
    if score >= high_score:
        high_score = score
    #end of if
#end of for
        
print(f"The highest score is {high_score}")
