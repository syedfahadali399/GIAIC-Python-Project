def calculator(x, operator, y):
    result = eval(f'{x} {operator} {y}')
    return result

def main():
    number_1 = str(input("Enter First Number: "))
    operator = str(input("Enter any operator: "))
    number_2 = str(input("Enter Second Number: "))

    perform = calculator(number_1, operator, number_2)
    print(f"The Result is {perform}")

main()