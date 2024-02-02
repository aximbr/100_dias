#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# num_words = len(word_list)
# word_index = random.randint(0, num_words-1)

#chosen_word = word_list[word_index]
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for i in range(len(chosen_word)):
#     if (chosen_word[i] == guess):
#          print("Right")
#     else:
#          print("Wrong")
  
for i in chosen_word:
    if i == guess:
         print("Right")
    else:
         print("Wrong")