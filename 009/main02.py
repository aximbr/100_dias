students_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

#TODO-1 create a new empty called dictionarie students_grades 

students_grades = {}

#TODO-2 convert students scores to grades 
#91 - 100 = "Outstandig"
#81 - 90 = "Exceed Expectations"
#71 - 80 = "Acceptable"
#70 - lower = "Fail"
for key in students_scores:
    if students_scores[key] > 90:
        students_grades[key] = "Outstanding"
    elif students_scores[key] >80:
        students_grades[key] = "Exceed Expectations"
    elif students_scores[key] >70:
        students_grades[key] = "Acceptable"
    else:
        students_grades[key] = "Fail"

for key in students_grades:
    print(f"{key} {students_grades[key]}")
    