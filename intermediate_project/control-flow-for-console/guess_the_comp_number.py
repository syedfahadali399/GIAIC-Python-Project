import random
from time import sleep

sleep(0.3)
ask = int(input("How Many Times Did you play the game: "))

def game(r):

    pionts = 0

    for r in range(0, r):
       
       sleep(0.4)
       print("")
       print("Welcome To High-low Game!")
       sleep(0.4)
       print("-------------------------")
       print("")

       user_number = random.randint(1, 100)
       comp_number = random.randint(1,100)
       hidden = "hidden"

       while user_number != comp_number:
            
            sleep(0.4)
            print(f"Round {r + 1}")
            sleep(0.4)
            print(f"Your Number is {user_number}")
            sleep(0.4)
            print(f"The Computer number is {hidden}")

            sleep(0.4)
            ask_user = str(input("Do you think your number is higher or lower than the computer's?: ")).lower()

            if(ask_user == "l"):
                if(user_number < comp_number):
                    sleep(0.3)
                    print(f"You were right! The computer's number was {comp_number}")
                    pionts += 1
                elif(user_number > comp_number):
                    sleep(0.3)
                    print(f"Aww, that's incorrect. The computer's number was {comp_number}")

            elif(ask_user == "h"):
                if(user_number > comp_number):
                    sleep(0.3)
                    print(f"You were right! The computer's number was a {comp_number}")
                    pionts += 1
                elif(user_number < comp_number):
                    sleep(0.3)
                    print(f"Aww, that's incorrect. The computer's number was a {comp_number}")
            else:
                sleep(0.3)
                print("Please Enter correct letter")

            break

       else:
           sleep(0.3)
           print(f"Your Number {user_number} and computer Number {comp_number} are same")
           break
       
    print("")
    print(f"Your Total Score is {pionts}")
               
           
game(ask)