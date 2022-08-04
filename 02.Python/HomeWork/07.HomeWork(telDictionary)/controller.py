import interface as UI
import read_from_database as DB
import search as SI
import data_output as DOUTPUT
import creation_row as CROW
import dictionaries as DIC
import phone_number_del as DEL
import change_item as CHANGE

def one_card_or_multi(card):
    if len(card) > 1:
        DOUTPUT.colums_output(DIC.row_phone_number,card)
    else :
        DOUTPUT.card_output(DIC.row_phone_number,card)

def look_on_contact():
    option_value = UI.search_var ()
    match option_value:
            case 1:
                name = "Alexander" 
                card = SI.search_by_name(name,DB.take_from_base())
                one_card_or_multi(card)
            case 2:
                name = "Alexander" 
                sir_name = "Maksaimer" 
                card = SI.search_by_name_surname(name,sir_name,DB.take_from_base())
                one_card_or_multi(card)
            case 3:
                tel = "+7 900 000 00 21" 
                card = SI.search_by_phone_number(tel,DB.take_from_base())
                one_card_or_multi(card)
def button():
    UI.description()
    user_name = UI.hello()
    repeat = 2
    while repeat == 2:
        option_value = UI.input_options()
        match option_value:
            case 1:
                look_on_contact()
            case 2:
                repeat_val = True
                while repeat_val:
                        # Блок ввода информации для карточки
                    First_name = "Alexander"
                    Last_name = "Maksaimer"
                    Other_name = " "
                    gender = 1
                    contact_type = 3
                    tel_number = "+7 495 622 00 41"

                    new_card = CROW.glossary_creation\
                            (
                                    First_name = First_name, 
                                    Last_name = Last_name, 
                                    Other_name = Other_name,
                                    gender = gender ,
                                    type_of_contact = contact_type, 
                                    phone_number = tel_number,
                                    data = DB.take_from_base()
                            )
                    DOUTPUT.card_output(DIC.row_phone_number,new_card)
                    DB.rewrite_base(new_card)
                    repeat_val = UI.repeat_options() 
            case 3:
                option_value = UI.options_what_to_do()
                match option_value:
                    case 1:
                        look_on_contact()
                        option_value = UI.options_find_contact()
                        match option_value:
                            case 1:
                                print("Ищем")
                            case 2:
                                repeat_val = True
                                while repeat_val:
                                    ID_user = "3" 
                                    What_to_change = 1 
                                    new_name = "Максим"
                                    dict_2 = DB.take_from_base()
                                    data = CHANGE.change_item_in_dict(ID_user,DIC.row_phone_number[What_to_change],new_name,dict_2)
                                    DB.rewrite_base(data)
                                    DOUTPUT.card_output(DIC.row_phone_number,data)
                                    repeat_val = UI.repeat_options()
                            case 3:
                                repeat_val = True
                                while repeat_val:
                                    ID_user = input("Выберите ID контакта для удаления") 
                                    DEL.del_row(ID_user)
                                    repeat_val = UI.repeat_options()
        repeat = UI.finish (user_name = user_name)