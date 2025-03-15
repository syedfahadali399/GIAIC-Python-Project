def print_ones_digit(num):
    print(f"The ones digit is {num % 10}")

def main():
    prompt = int(input("Enter an integer number: "))
    print_ones_digit(prompt)

main()