from time import sleep

sleep(0.5)
print("")
print("Welcome To Planetry Weight Calculator! ")
print("")
sleep(0.5)
user_weight = int(input("Enter a weight on Earth in kg: "))
sleep(0.5)
planet_name = str(input("Enter a Planet Full Name: ")).lower().strip()

def func(weight, name):

    plantry_weight = {
        "mercury": 3.70,
        "venus": 8.87,
        "mars": 3.71,
        "jupiter": 24.79,
        "saturn": 10.44,
        "uranus": 8.69,
        "neptune": 11.15
    }

    if name in plantry_weight.keys():
        cal = plantry_weight[name] / 9.81
        cal_weight = weight * cal

    elif name == "pluto":
        print("Pluto is a drawf Planet")
    else:
        print("Please Enter Correct Planet Name!")
    
    round_value = round(cal_weight, 2)
    return round_value


result = func(user_weight, planet_name)
sleep(0.4)
print("Calculating Weight...")
sleep(0.8)
print("")
print(f"The {user_weight}kg Weight On Earth is Equal to {result}kg Weight On Planet {planet_name.capitalize()}")