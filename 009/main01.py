#Day 9 - Dictionaries on Python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#printing all elements from dictionay
print(programming_dictionary)

#add a new item on existing dictionary
programming_dictionary["New"] = "Something that not happened yet."

print(programming_dictionary)

#create an empty dictionary
new_dictionary = {}

#add item
new_dictionary[0] = "number zero"

#accessing
print(new_dictionary[0])

#cleanning a dictionary
new_dictionary={}
print(new_dictionary)

#using in a loop
for x in programming_dictionary:
    print(x)
    print(programming_dictionary[x])



