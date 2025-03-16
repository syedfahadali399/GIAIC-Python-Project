def double(num):
    cal = num * 2
    return cal

def main():
    print("Welcome to number Doubler!")
    prompt = int(input("Enter any Number: "))
    get_ans = double(prompt)
    print(get_ans)

main()