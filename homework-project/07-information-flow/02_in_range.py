import random
def in_range(n, low, high):
    if n >= low and n <= high:
        return True

    return False

def main():
    num_1 = int(input("Enter Number between 1 to 10: "))
    # random_num = random.choice(2, 10)
    print(in_range(num_1, 1, 10))

main()