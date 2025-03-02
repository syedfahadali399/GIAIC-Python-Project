def add_numbers(numbers):

    total = 0
    for number in numbers:
        total += number
    return total


def main():
    numbers: list = [1, 2, 3, 4, 5]
    add_two_number = add_numbers(numbers)
    print(add_two_number)

main()