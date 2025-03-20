def phone_book():
    book = {}

    while True:
        name = input("Enter user name: ")
        if name == " ":
            break
        number = input("Enter user Number: ")
        book[name] = number
    
    return book

def print_book(book):

    for name in book:
        print(f"{name} => {book[name]}")

def look_up(book):

    while True:
        name = input("Enter user name: ")
        if name == " ":
           break
        if name not in book:
            print(f"{name} is not in the PhoneBook")
        else:
            print(f"Name = {name} || Number = {book[name]}")



def main():
    book = phone_book()
    print_book(book)
    look_up(book)

main()