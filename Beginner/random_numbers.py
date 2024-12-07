import random

#random_integer = random.randint(1, 49)
#print(random_integer)

#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)

#random_float = random.uniform(1, 10)
#print(random_float)

a = random.randint(1, 10)
b = random.randint(1, 10)

if a > b:
    print(f"Number {a} is bigger than number {b}")
elif a == b :
    print(f"Number {a} is equal to number {b}")    
else:
    print(f"Number {a} is smaller than number {b}")  

