height = float(input("Enter your height in m: "))
weight =  float(input("Enter your weight in kg: "))
# TODO
bmi = round(weight / height ** 2,2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, your weight is underweight.")
elif bmi< 25:
    print(f"Your bmi is {bmi}, your weight is normal.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, your weight is overweight.")
else:
    print(f"Your bmi is {bmi}, your weight is obese.")