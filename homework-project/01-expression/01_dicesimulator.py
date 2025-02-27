import random

def dice():
    dice_one = random.randint(0,6)
    dice_two = random.randint(0,6)
    dice_result = dice_one + dice_two
    return dice_result

def main():
    print(f"The First Dice Result is {dice()}")
    print(f"The Second Dice Result is {dice()}")
    print(f"The Third Dice Result is {dice()}")

main()