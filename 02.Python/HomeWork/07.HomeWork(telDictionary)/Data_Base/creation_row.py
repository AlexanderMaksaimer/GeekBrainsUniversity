# задача - получит от пользователя данные, и создать кортеж 

import dict as Dic

def row_creation_fun \
    (
        First_name = " ", 
        Last_name = " ", 
        Other_name = " ",
        sex = 0 ,
        type_of_contact = 0, 
        tel_number = "",
        data = {}
        
    ):
    phone_dic = data
    person_info = \
        {
            "First name" : First_name ,
            "Second name" : Last_name , 
            "Othen name" : Other_name ,
            "Sex" : Dic.sex_dic[sex] ,
            "Type of Contact" : Dic.type_of_contact_dic[type_of_contact] , 
            "Tel number" : tel_number
        }
    if len(data) == 0:
        phone_dic[0] = person_info
    else :
        phone_dic[int(max(phone_dic.keys()))+1] = person_info
    return phone_dic
