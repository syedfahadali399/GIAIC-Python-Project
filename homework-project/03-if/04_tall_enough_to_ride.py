ask_user = int(input("Enter Your Height: "))

def main(height):
    min_height = 50

    while height <= min_height:
        print("You're not tall enough to ride, but maybe next year!")
        height = int(input("Enter Your Height: "))
    else:
        print("You're tall enough to ride!")

main(ask_user)