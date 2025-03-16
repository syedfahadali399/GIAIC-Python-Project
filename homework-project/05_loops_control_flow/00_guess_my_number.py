import random

def num_guess(num):

    random_num = random.randint(1, 100)

    while num != random_num:

        if num < random_num:
          print("Your Guess is low!")
        elif num > random_num:
          print("Your Guess is high!")

        num = int(input("Enter number b/w 1 to 100: "))

    else:
       print(f"Your Number {num} and Computer {random_num} num is same")


def main():
    print("Welcome to number guesser game!")
    num = int(input("Enter number b/w 1 to 100: "))
    num_guess(num)

main()