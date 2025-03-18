def even_val(num):
    for i in range(num): 
       print(i * 2)

def main():
    prompt = int(input("How many number of even value: "))
    even_val(prompt)

main()