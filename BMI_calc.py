def test_input(height, weight):
    """
    :param height: (float) height in cm
    :param weight: (float) weight in cm
    :return: True/False
    """
    if type(height) and type(weight) not in [int, float]:
        raise TypeError('The provided value is not a float')
    else:
        if height <= 0 or weight <= 0:
            print("Invalid input")
            return False
        return height, weight # True


def bmi_calc():

    while True:
        try:
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kg: "))
            if (height <= 0) or (weight <= 0):
                print("Value can not be zero or negative")
        except ValueError:
            print("The provided value is not a float")
        else:
            if (height > 0) and (weight > 0):
                break
    if test_input(height, weight):
        bmi = weight / (height / 100) ** 2
        print(f"Your bmi is {bmi}")
        if bmi <= 18.5:
            print("You are underweight.")
        elif bmi <= 25:
            print("You are healthy.")
        else:
            print("You are over weight.")


bmi_calc()

"""
Round 1 of tests: (input)
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
"""
