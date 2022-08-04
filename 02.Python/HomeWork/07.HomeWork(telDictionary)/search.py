# поиски

def search_by_name(name , data : dict):
    return dict(filter(lambda x : x[1]["Имя"] == name , data.items()))

def search_by_name_surname(name , sur_name, data : dict):
        return dict(filter(lambda x : x[1]["Имя"] == name and x[1]["Фамилия"] == sur_name  , data.items()))

def search_by_phone_number(phone_number, data : dict):
        return dict(filter(lambda x : x[1]["Номер телефона"]==  phone_number, data.items()))

def search_by_gender(gender, data : dict):
        return dict(filter(lambda x : x[1]["Пол"]==  gender, data.items()))

def search_by_contact_type(contact_type, data : dict):
        return dict(filter(lambda x : x[1]["Тип(вид) контакта"]==  contact_type, data.items()))
