print("Welcome!")
height = int(input("Please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age: "))
    if age > 18:
        bill = 12
        print("You must pay $12 to ride.")
    elif age <= 18 and age >= 12 :
        bill = 7
        print("You must pay $7 to ride.")
    else: 
        bill = 5
        print("You must pay $5 to ride.")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.") 
    if wants_photo == "y" :
        #Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")    
 
else:
    print("Sorry! You can not ride.")        

     