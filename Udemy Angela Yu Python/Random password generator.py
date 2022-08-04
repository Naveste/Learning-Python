import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(0, nr_letters): #loops from index to user input amount, e.g 2, 0 -> 1
    random_char = random.choice(letters) #chooses random item from the variable letters.
    password_list.append(random_char) #adds the randomly chosen item to password_list.

for num in range(0, nr_numbers):
    random_num = random.choice(numbers)
    password_list.append(random_num)

for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

random.shuffle(password_list) #shuffles around the items in password_list
password = "" #store shuffled password here
for pw in password_list: #for every item in password_list
    password += pw #add them to the variable password

print(password)