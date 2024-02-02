# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
fonetic = {row.letter:row.code for (index, row) in df.iterrows()}

#print(fonetic)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Enter a Word: ").upper()

spell =[]
#Solution 1
# for letter in word_input:
#     for (index, row) in df.iterrows():
#         if row.letter == letter:
#             spell.append(row.code)

#Solution 2            
# for letter in word_input:
#     spell.append(fonetic[letter])

#Solution 3
spell = [fonetic[letter] for letter in word_input]
        
        
print(spell)
    


