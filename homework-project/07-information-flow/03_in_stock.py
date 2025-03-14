def fruit_in_stock(fruit_name):
    if fruit_name == "apple":
        return 20
    elif fruit_name == "banana":
        return 14
    elif fruit_name == "mango":
        return 18
    elif fruit_name == "pineapple":
        return 5
    else: 
        return 0
    
def store():
    prompt = str(input("Enter Fruit Name To Check your Stock: ").lower())
    check = fruit_in_stock(prompt)
    if check == 0:
        print("Stock Has Been Out")
    else:
        print(f"Congrats {prompt} Stock Has Been in WareHouse")
        print(check)
store()
