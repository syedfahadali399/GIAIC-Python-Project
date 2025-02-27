def triangle_lenght():
    lenght_side_1 = float(input("Enter 1st Side of Triangle Length: "))
    lenght_side_2 = float(input("Enter 2nd Side of Triangle Length: "))
    lenght_side_3 = float(input("Enter 3rd Side of Triangle Length: "))

    result = lenght_side_1 + lenght_side_2 + lenght_side_3
    return result

show_result = triangle_lenght()
print(f"The Total Triangle Length is {show_result}")
