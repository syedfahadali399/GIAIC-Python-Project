def get_name():
    prompt = str(input("Enter Your Name: "))
    return prompt

def main():
    name = get_name()
    print(f"Hello {name.capitalize()}")


main()