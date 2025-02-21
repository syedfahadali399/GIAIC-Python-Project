from random import choice

repeat_program = int(input("How Many you have to play game: "))

def game(r):

    for r in range(0, r):

        user_input = str(input("""Enter any word from => \n(r, p, s) to play game: """))
        game_choices = ["r", "p", "s"]
        random_chioce = choice(game_choices)
    
        if(user_input == random_chioce):
            print("Its Draw")
        elif(user_input == "r" and random_chioce == "p"):
            print("You Lose")
        elif(user_input == "r" and random_chioce == "s"):
            print("You Win")
        elif(user_input == "p" and random_chioce == "r"):
            print("You Win")
        elif(user_input == "p" and random_chioce == "s"):
            print("You Lose")
        elif(user_input == "s" and random_chioce == "r"):
            print("You Lose")
        elif(user_input == "s" and random_chioce == "p"):
            print("You Win")
        else:
            print("Please Enter (r, p, s) to play game: ")
    r += 1

game(repeat_program)