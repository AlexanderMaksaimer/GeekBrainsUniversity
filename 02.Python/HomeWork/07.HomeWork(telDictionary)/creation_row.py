# задача - получить от пользователя данные, и создать кортеж 

import dictionaries as GLO
def glossary_creation \
    (
        First_name = " ", 
        Last_name = " ", 
        Other_name = " ",
        gender = 0 ,
        type_of_contact = 0,
        birthday = "",
        addres = "",
        workplace = "", 
        phone_number = "",
        data = {}
        
    ):
    phone_dic = data
    information_contact_dictionary = \
        {
            "Имя" : First_name ,
            "Фамилия" : Last_name , 
            "Отчество (при наличии)" : Other_name ,
            "Пол" : GLO.gender_dictionary[gender] ,
            "Тип(вид) контакта" : GLO.contact_type_dictionary[type_of_contact] , 
            "Дата рождения" : GLO.birthday_date_dictionary[birthday],
            "Адрес" : GLO.addres_dictionary[addres],
            "Место работы" : GLO.work_place_dictionary[workplace],
            "Номер телефона" : phone_number
        }
    if len(data) == 0:
        phone_dic[0] = information_contact_dictionary
    else :
        phone_dic[int(max(phone_dic.keys()))+1] = information_contact_dictionary
    return phone_dic
