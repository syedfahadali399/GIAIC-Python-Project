import time

fruit_list = {
    "apple": 200,
    "banana": 150,
    "mango": 300,
    "pineapple": 550,
    "grapes": 250
}

def fruit(name):
    total_cost = 0
    print("Welcome to Grocessry store")
    for fruit_name in name:
        time.sleep(1)
        prompt = input(f"Do You want to Buy {fruit_name}: ").lower().strip()
        if prompt == "yes":
            price = name[fruit_name]
            time.sleep(0.25)
            print(f"The Price of {fruit_name} is {price}")
            time.sleep(0.25)
            total_cost += price
        elif prompt == "no":
            print("Part Skip!")
        else:
            print("Please Enter correct keyword")

    print(f"The Total Price of item is {total_cost}")


fruit(fruit_list)
