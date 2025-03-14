ask_user = int(input("Enter Your Age: "))

def is_adult(age):
    if age >= 18:
        return True
    return False

result = is_adult(ask_user)
print(result)