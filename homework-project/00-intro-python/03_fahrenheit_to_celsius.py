def fahren_cel():
    input_user = float(input("Enter Fahrenheit Temprature in your area: "))

    cal = (input_user - 32) * 5 / 9
    return cal

show_value = fahren_cel()
print(f"The Temprature in Celsius is {round(show_value, 2)}°C")