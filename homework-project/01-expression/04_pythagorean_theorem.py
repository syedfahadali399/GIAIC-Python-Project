import math

def pythagorean_theorem():
    input_AB = float(input("Enter the length of AB: "))
    input_AC = float(input("Enter the length of AC: "))

    cal: float = math.sqrt(input_AB**2 + input_AC**2)
    return cal

show_result = pythagorean_theorem()
print(f"The length of BC (the hypotenuse) is: {show_result}")