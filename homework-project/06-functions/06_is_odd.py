def even_odd(num):
    for i in range(0, num):
        if is_odd(i):
            print(f"odd {i}")
        else:
            print(f"Even {i}")

def is_odd(value:int):
    
    remainder = value % 2 
    return remainder == 1 

def main():
    prompt = int(input("Enter any Number: "))
    even_odd(prompt)

main()