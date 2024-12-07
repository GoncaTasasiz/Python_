weight = int(input("Enter your weight in kg "))
height = float(input("Enter your height in m "))
bmi = round(weight / (height ** 2), 2)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
else:
    print("Overweight")       
 