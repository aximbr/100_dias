#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
TEMPLATE_LETTER = "Letters/starting_letter.txt"
LIST_NAMES = "Names/invited_names.txt"
INPUT_PATH = "./Input/"
OUTPUT_PATH = "./Output/ReadyToSend/"
PREFIX_NAME = "letter_"
SUFIX_NAME = ".txt"
PLACEHOLDER = "[name]"

names = []

#Load message template
with open(INPUT_PATH + TEMPLATE_LETTER, "r") as fp:
    message_template = fp.read()

#Load list of names
with open(INPUT_PATH + LIST_NAMES, "r") as fp:
    names_temp = fp.readlines()
    for name in names_temp:
        names.append(name.strip())

#write_letter()
for name in names:
    new_message = message_template.replace(PLACEHOLDER, name)
    with open(OUTPUT_PATH + PREFIX_NAME + name + SUFIX_NAME, "w") as fp:
        fp.write(new_message)
    

