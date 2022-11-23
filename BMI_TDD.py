def test_input():  # Step 1: Test func for the input
    # Step 3: The function has been improved - Input error friendly
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kg: "))
        except ValueError:
            print('The provided value is not a float')
        else:
            break
    if height <= 0 or weight <= 0:
        return 0, 0
    else:
        return height, weight


# Step 2: Run test function
(h,w) = test_input()
if (h,w) == (0, 0):
    print("Invalid input")
else:
    BMI = w / (h / 100) ** 2
    print(f"Your BMI is {BMI}")
    if BMI <= 18.5:
        print("You are underweight.")
    elif BMI <= 25:
        print("You are healthy.")
    else:
        print("You are over weight.")