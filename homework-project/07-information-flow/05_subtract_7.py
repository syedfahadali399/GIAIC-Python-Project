def subtract_seven(num):
    greater_num = 7
    cal = greater_num - num
    return cal

def main():
    num = int(input("Enter Number between 1 to 7: "))
    print(subtract_seven(num))

main()