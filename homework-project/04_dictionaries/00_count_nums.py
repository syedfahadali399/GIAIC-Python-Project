def track_number():
    num_list = []

    while True:
        num_input = input("Enter any Number to add in the list: ")
        if num_input == " ":
            break

        num = int(num_input)
        num_list.append(num)  

    return num_list

def count_num(num_list):

    num_dict = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict

def print_counts(num_dict):

    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
   number_list = track_number()
   count_result = count_num(number_list)
   print(count_result)
   print_counts(count_result)   

main()