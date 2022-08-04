from caesar_art import *
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, direction):
  
  final_text = ""

  for letter in start_text: #start with the first index of the chosen text. In this case with hello, it starts with "h"
    if letter in alphabet: #allow only if letter is in the variable alphabet
      position = alphabet.index(letter) #show its position in the variable alphabet, in this case for "h" is at 7.
      if direction == 'encode':
        new_position = position + shift_amount  #show its new position by adding it with user's input "shift", e.g shift 4 = previous position(7) + 4 = 11
      else:
        new_position = position - shift_amount
      new_letter = alphabet[new_position] #new letter is now "l" due to its position being index 11 in the alphabet.
      final_text += new_letter #add "l", which is at index 11 in the chosen text, to final_text. Repeat process for the rest of the letters in the chosen text.

  if direction == 'encode':
    print(f"The encoded text is {final_text}")
  else:
      print(f"The decoded text is {final_text}")

# divide code by 26 infinitely until it cant be fully divided and end with a remainder.
shift = shift % 26

while True:
  caesar(start_text=text, shift_amount=shift, direction=direction)
  try_again = input("Want to try again? Yes or no: ").lower()
  if try_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  elif try_again == 'no':
    break