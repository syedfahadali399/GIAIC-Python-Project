ask_num = int(input("Enter a Number to double the value: "))

def square_number(value):

    result = value * 2
    return result

show_result = square_number(ask_num)
print(f"The Square value of {ask_num} is {show_result}")