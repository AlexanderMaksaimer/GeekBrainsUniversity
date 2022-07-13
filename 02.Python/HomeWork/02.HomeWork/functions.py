import random

def input_number_test(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else :
            print("Not a number , try again")
    return coord

def input_number_test_not_minus(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
            print("Entered number < 0 , took +")
        if coord.isdigit():
            coord = int(coord)
            int_test = False
        else :
            print("Not a number , try again")
    return coord

def input_number_test_float(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        elif coord.isdecimal:
            coord = float(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else :
            print("Not a number , try again")
    return coord

def input_number_test_biger_then_zero(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if coord <= 0:
                print("Enter number > 0")
            else:
                int_test = False
        else :
            print("Not a number , try again")
    return coord

def random_array_creation(elements,min_number,max_number):
    list_of_numbers =[]
    for i in range(0,elements):
        list_of_numbers.append(random.randrange(min_number,max_number+1))
    return list_of_numbers