number = int(input("Type a number to learn if it is even or odd ")) 
number_check = number % 2
if number_check == 0:
    print(f"Number {number} is even")
else:
    print(f"Number {number} is odd")
