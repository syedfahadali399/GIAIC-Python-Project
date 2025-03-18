def double_num(num, end_num):
    while num < end_num:
        num = num * 2
        if num < end_num:
           print(num, end=" ")
    else:
        print(f"\nYour end piont num is {end_num}")


def main():
    prompt = int(input("Enter any number to double that number: "))
    end_piont = int(input("Enter end point of the number that double will stop: "))
    double_num(prompt, end_piont)

main()