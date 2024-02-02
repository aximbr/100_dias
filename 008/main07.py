#better solution for previus problem (see main06.py)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text_in, shift_in, direction_in):
 
    output_text = ""
    if direction_in == "decode":
        shift_in *= -1
    for letter in text_in:
        position = alphabet.index(letter)
        new_position = position + shift_in
        output_text += alphabet[new_position]
 
   
    print(f"The {direction_in}d text is {output_text}")
   



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text_in = text, shift_in= shift, direction_in= direction)