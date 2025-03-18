affirmation = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {affirmation}")

    user_feedback = str(input())
    while user_feedback != affirmation:
        print("That was not the affirmation.")

        print(f"Please type the following affirmation: {affirmation}")
        user_feedback = input()
    else:
      print("That's right! :)")

main()