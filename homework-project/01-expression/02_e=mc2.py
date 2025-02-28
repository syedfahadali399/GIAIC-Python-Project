import time

def mass():
    c = 299792458
    input_user = float(input("Enter the Mass in Kilo: "))

    e = input_user * (c**2)
    return e

show_result = mass()
time.sleep(1)
print(f"{show_result} joules of energy!")