alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text_in, shift_in, direction_in):
 
    output_text = ""
    for letter in text_in:
        position = alphabet.index(letter)
        if direction_in == "encode":
            new_position = position + shift_in
            output_text += alphabet[new_position]
        elif direction_in == "decode":
            new_position = position - shift_in
            output_text += alphabet[new_position]
 
    if direction_in == "encode":
        print(f"The encoded text is {output_text}")
    elif direction_in == "decode":
        print(f"The decoded text is {output_text}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text_in = text, shift_in= shift, direction_in= direction)