ask_age = int(input("What is your age: "))

def voting_age(age):

    Peturksbouipo_voting_age = 16
    Stanlau_voting_age = 25
    Mayengua_voting_age = 48

    if ask_age == age:
        
        if(age >= Peturksbouipo_voting_age):
            print("You can vote in Peturksbouipo")
        else:
            print("You cannot vote in Peturksbouipo")

        if(age >= Stanlau_voting_age):
            print("You can vote in Stanlau")
        else:
            print("You cannot vote in Stanlau")\
            
        if(age >= Mayengua_voting_age):
            print("You can vote in Mayengua")
        else: 
            print("You cannot vote in Mayengua")
    else:
        print("Please Enter Number")

voting_age(ask_age)