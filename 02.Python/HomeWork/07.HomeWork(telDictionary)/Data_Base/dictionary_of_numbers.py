# задача - получит от пользователя данные, и создать кортеж 
# Изначальная идея базы данных - для простоты упростил её

import dict as Dic

def phone_number_row_creation \
    (
        First_name = " ", 
        Last_name = " ", 
        Other_name = " ",
        type_of_contact = 0, 
        sex = 0 ,
        bithd_day = " ",
        Commentary = " " ,
        Company_name = " ",
        fav_check = False ,
        type_of_number = 0 ,
        tel_number = " ",
        telefon_comment = "" ,
        email = " ",
        data = {}
        
    ):
    """Метод - принимает на вход параметры телефонного справочника, если они не заданы - использует значения по умолчанию
    Перед началом загружает справочник , для того что бы подобрать последний ключ и новый добавлять по новому ключу 
    возвращает словарь - строчку с данными
    """
    phone_dic = data
    tel_number_dic = \
        {
            "Telefon type" : Dic.tel_type_dic[type_of_number] ,
            "Telefon number" : tel_number ,
            "Telefon comment" : telefon_comment,
            "E-mail" : email  
        } 
    person_info = \
        {
            "First name" : First_name ,
            "Second name" : Last_name , 
            "Othen name" : Other_name ,
            "Type of Contact" : Dic.type_of_contact_dic[type_of_contact] , 
            "Sex" : Dic.sex_dic[sex] ,
            "Birth Day" : bithd_day ,
            "Comment" : Commentary ,
            "Company" : Company_name ,
            "Fav check" : fav_check,
            "Tel_info" : tel_number_dic
        }
    phone_dic[int(max(phone_dic.keys()))+1] = person_info
    return phone_dic
