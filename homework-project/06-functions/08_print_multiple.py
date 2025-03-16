def print_message(message, repeat):
    for i in range(repeat):
        print(message)
        i += 1



def main():
    print("Welcome! to printer message")
    prompt = str(input("Enter your message: "))
    repeat = int(input("How many do you want to print that message: "))
    print_message(prompt, repeat)

main()