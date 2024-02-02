#Day 026 List comprehension
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [n*n for n in numbers]

# print(squared_numbers)

# even_numbers = [n for n in numbers if n%2 == 0]

# print(even_numbers)

# with open("file1.txt", "r") as fp:
#     file1 = fp.readlines()

# with open("file2.txt", "r") as fp:
#     file2 = fp.readlines()   

    
# new_list = [int(n) for n in file1 if n in file2]
# print(new_list)

# new_dictionary = { new_key:new_value for item in list if test}

# new_dictionary = { new_key:new_value for (key, value) in dict.items() if test}

# 
# setence = "What is the Airspeed Velocity of an Unladen Swallow?"

# setence_list = setence.split()
# print(setence_list)

# result = { word:len(word) for word in setence_list}

# print(result)

# weather_c = { 
#             "Monday" : 12,
#             "Tuesday": 14,
#             "Wednesday" : 15,
#             "Thursday" : 14,
#             "Friday": 21,
#             "Saturday": 22,
#             "Sunday" : 24
#             }
# weather_f = {key: temp*9/5 +32 for (key, temp) in weather_c.items()}

# print(weather_f)

student_dict ={ 
               "Student" : ["Angela", "James", "Lily"],
               "Score": [ 56, 76, 98]
               }
import pandas

student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key)
  
# for (key, value) in student_data_frame.items():
#     print(value) 
    
# for (index, row) in student_data_frame.iterrows():
#     print(row) 
# for (index, row) in student_data_frame.iterrows():
#     print(row.Student) 
    
# for (index, row) in student_data_frame.iterrows():
#     print(row.Score)
    
for (index, row) in student_data_frame.iterrows():
    if row.Student == "Angela":
        print(row.Score)