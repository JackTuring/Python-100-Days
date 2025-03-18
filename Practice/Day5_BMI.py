height = float(input("Please enter your height in cm: "))
weight = float(input("Please enter your weight in kg: "))
BMI = weight / (height/100) ** 2
if 18.5 <= BMI <= 24:
    print(f"Your BMI is {BMI:.1f}, you are in good health")
else:
    print(f"Your BMI is {BMI:.1f}, you should pay more attention to your body")