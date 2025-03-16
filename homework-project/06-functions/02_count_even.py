def even_lst(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1

    print(count)



def add_num():
    lst = []
    prompt = input("Enter Number to add in the list & press enter to stop: ")
    while prompt != " ":
        lst.append(int(prompt))
        prompt = input("Enter Number to add in the list & press enter to stop: ")

    return lst

def main():
    lst = add_num()
    even_lst(lst)

main()
