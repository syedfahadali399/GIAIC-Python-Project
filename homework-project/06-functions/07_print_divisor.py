def print_divisors(num):

    for i in range(num):
        curr_divisor = i + 1 
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    print("Welcome! to Divisor number")
    prompt = int(input("Enter any Number: "))
    print_divisors(prompt)

main()