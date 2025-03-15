def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Enter Number b/w 0 to 2")



def main():
    prompt = str(input("Enter type a noun, verb or adjective word: "))
    print("Is this a noun, verb, or adjective?")
    choose = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(prompt.capitalize(), choose)
 
main()