# curr_value = int(input("Enter a number: "))

# while curr_value < 100:
#     curr_value = curr_value * 2 
#     print(curr_value, end=" ")

total = 0

while total < 100:
    try:
        num = int(input("Enter a number: "))
        
        doubled = num * 2
        total += doubled 
        
        print(f"{num} doubled is {doubled}. Total so far: {total}")
        
        if total >= 100:
            print("The total has reached or exceeded 100. Exiting...")
            break
        else:
            print("The total is less than 100. Please enter another number.\n")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")



