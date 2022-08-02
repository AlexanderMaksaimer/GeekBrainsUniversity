# задача - получить от пользователя данные, и создать кортеж 

import Dictionary as GLO

def phone_number_cortege \
    (
        First_name = " ", 
        Last_name = " ", 
        Other_name = " ",
        type_of_contact = 0, 
        gender = 0 ,
        bitrhday = " ",
        addres = " ",
        Commentary = " " ,
        Workplace = " ",
        type_of_number = 0 ,
        phone_number = " ",
        discription = "" ,
        email = " ",
        data = {}
        
    ):
    """Метод - принимает на вход параметры телефонного справочника, если они не заданы - использует значения по умолчанию
    Перед началом загружает справочник , для того что бы подобрать последний ключ и новый добавлять по новому ключу 
    возвращает словарь - строчку с данными
    """
    phone_numbers = data
    telephone_number_dict = \
        {
            "Тип номера телефона" : GLO.phone_number_dictionary[type_of_number] ,
            "Номер телефона" : phone_number ,
            "Комментарий" : discription,
            "E-mail" : email  
        } 
    person_info = \
        {
            "Имя" : First_name ,
            "Фамилия" : Last_name , 
            "Отчество" : Other_name ,
            "Тип контакта" : GLO.contact_type_dictionary[type_of_contact] , 
            "Пол" : GLO.gender_dictionary[gender] ,
            "Дата рождения" : GLO.bitrhday_date_dictionary[bitrhday] ,
            "Адрес" : GLO.addres_dictionary [addres],
            "Комментарий" : Commentary ,
            "Место работы" : GLO.work_place_dictionary [Workplace],
            "Информация о номере" : telephone_number_dict
        }
    phone_numbers[int(max(phone_numbers.keys()))+1] = person_info
    return phone_numbers
