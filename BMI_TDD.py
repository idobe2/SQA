def testInput():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    if height < 0 or weight < 0:
        return False
    else:
        return weight / (height / 100) ** 2


BMI = testInput()
if BMI:
    print(f"Your BMI is {BMI}")
    if BMI <= 18.5:
        print("You are underweight.")
    elif BMI <= 25:
        print("You are healthy.")
    elif BMI <= 30:
        print("You are over weight.")
    elif BMI <= 35:
        print("You are severely over weight.")
    elif BMI <= 40:
        print("You are obese.")
    else:
        print("You are over weight.")
else:
    print("Invalid input")
