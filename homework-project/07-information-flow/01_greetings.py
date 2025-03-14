def greeting(name):
    return f"Hello {name}"

def main():
    input_user = str(input("Enter Your Name: "))
    print(greeting(input_user.capitalize().strip()))

main()   