import random
import time

def rolldice():
    roll_dice_1: int = random.randint(0, 6)
    roll_dice_2: int = random.randint(0, 6)

    total = roll_dice_1 + roll_dice_2

    time.sleep(0.5)
    print(f"The Dice 1 value is {roll_dice_1}")
    time.sleep(0.5)
    print(f"The Dice 2 value is {roll_dice_2}")
    time.sleep(0.5)
    print(f"The Total value is {total}")

rolldice()