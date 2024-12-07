#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#First easy way
password_created = ""
for pw in range(1, nr_letters + 1):
    random_number = random.randint(1, len(letters)-1)
    add_pw = str(letters[random_number])
    password_created += add_pw
for pw in range(1, nr_symbols + 1):
    random_number = random.randint(1, len(numbers)-1)
    add_pw = str(numbers[random_number])
    password_created += add_pw   
for pw in range(1, nr_numbers + 1):
    random_number = random.randint(1, len(symbols)-1)
    add_pw = str(symbols[random_number])
    password_created += add_pw       
print(password_created)    

#Second easy way
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)    
for char in range(0, nr_numbers):
    password += random.choice(numbers)    

print(password)    

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#1. solution

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))    
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))    

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)    


#2. solution
def shuffle_string(string):
    char_list = list(string)
    random.shuffle(char_list)
    return ''.join(char_list)

shuffled_string = shuffle_string(password_created)
print(shuffled_string)
