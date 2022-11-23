def test_input(height, weight):
    if type(height) and type(weight) not in [int, float]:
        raise TypeError('The provided value is not a float')
        return 0, 0
    else:
        if height <= 0 or weight <= 0:
            print("Invalid input")
            return 0, 0
        return height, weight


def bmi_calc():
    """
    סבב ראשון של הבדיקות:
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = weight / (height / 100) ** 2
    print(f"Your bmi is {bmi}")
    if bmi <= 18.5:
        print("You are underweight.")
    elif bmi <= 25:
        print("You are healthy.")
    else:
        print("You are over weight.")
        סבב שני של הבדיקות:
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kg: "))
        except ValueError:
            print('The provided value is not a float')
            else:
                break
    test_input(height,weight)
    bmi = weight / (height / 100) ** 2
    print(f"Your bmi is {bmi}")
    if bmi <= 18.5:
        print("You are underweight.")
    elif bmi <= 25:
        print("You are healthy.")
    else:
        print("You are over weight.")
    """
    # הפונקציה לאחר תיקונים:
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kg: "))
            if (height <= 0) or (weight <= 0):
                print("Value can not be zero or negative")
        except ValueError:
            print('The provided value is not a float')
        else:
            if (height > 0) and (weight > 0):
                break
    test_input(height,weight)
    bmi = weight / (height / 100) ** 2
    print(f"Your bmi is {bmi}")
    if bmi <= 18.5:
        print("You are underweight.")
    elif bmi <= 25:
        print("You are healthy.")
    else:
        print("You are over weight.")



bmi_calc()
