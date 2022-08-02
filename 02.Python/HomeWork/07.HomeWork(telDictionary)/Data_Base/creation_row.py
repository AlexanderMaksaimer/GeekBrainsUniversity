# задача - получит от пользователя данные, и создать кортеж 

import Dictionary as GLO

def glossary_creation \
    (
        First_name = " ", 
        Last_name = " ", 
        Other_name = " ",
        gender = 0 ,
        type_of_contact = 0, 
        phone_number = "",
        data = {}
        
    ):
    phone_dic = data
    person_info = \
        {
            "First name" : First_name ,
            "Second name" : Last_name , 
            "Othen name" : Other_name ,
            "Sex" : GLO.gender_dictionary[gender] ,
            "Type of Contact" : GLO.contact_type_dictionary[type_of_contact] , 
            "Tel number" : phone_number
        }
    if len(data) == 0:
        phone_dic[0] = person_info
    else :
        phone_dic[int(max(phone_dic.keys()))+1] = person_info
    return phone_dic
