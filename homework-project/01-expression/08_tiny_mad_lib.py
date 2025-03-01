from time import sleep

def tiny_mad_lib():
    sleep(0.8)
    print("Welcome to Madlib Game!")
    sleep(0.8)
    print("Code in Place is fun. I learned to program and used Python to make my adjective noun verb!")
    prompt_1 = str(input("Enter an adjective word: "))
    prompt_2 = str(input("Enter a noun word: "))
    prompt_3 = str(input("Enter a verb word: "))
    sleep(1)
    print(f"Code in Place is fun. I learned to program and used Python to make my {prompt_1} {prompt_2} {prompt_3}!")
    sleep(0.3)
    print("End!")

tiny_mad_lib()