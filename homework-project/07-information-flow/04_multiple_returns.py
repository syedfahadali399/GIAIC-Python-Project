def get_user_data():
    first_name = str(input("Enter Your First Name: ").capitalize())
    last_name = str(input("Enter Your last Name: ").capitalize())
    email_address = str(input("Enter Your Email Address Name: "))
    return first_name, last_name, email_address

result = get_user_data()
print(result)

