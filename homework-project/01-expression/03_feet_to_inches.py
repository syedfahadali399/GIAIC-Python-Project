from time import sleep

def feet_to_inches():
    input_user = int(input("Enter your number of feet: "))

    cal = input_user * 12
    return cal

show_result = feet_to_inches()
sleep(1)
print(f"The number of feet you enter is eqivalent to {show_result} Inches")