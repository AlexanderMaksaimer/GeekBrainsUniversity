import dictionaries
from read_from_database import take_from_base as TAKE
from search import search_by_name

def FirstName():
            First_name = input("\nВедите имя контакта: ")
            data = search_by_name(First_name , TAKE())
            if len(data) < 1:
                print("нет такого пользователя")



def LastName():        
        Last_name = input("\nВведите фамилию: ") 



def OtherName():
            Other_name = input("\nВведите отчество (при наличии): ")

def gender(): 
    for i,itme in dictionaries.gender_dictionary.items():
        print(f"{i} - > {itme}")
        gender = input("\nВыберете пол: ")

def TypeOfContact():
    for i,itme in dictionaries.contact_type_dictionary.items():
        print(f"{i} - > {itme}")
        print("Выберите тип: ")
        Type_of_Contact = input("\nВыберите тип контакта из списка: ")

def Phone_Number():
        tel_number = input("\nВведите номер телефона: ")
