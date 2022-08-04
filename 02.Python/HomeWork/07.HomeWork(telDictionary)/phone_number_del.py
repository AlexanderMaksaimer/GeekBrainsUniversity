# Код удаления строчки из записной книжки

from read_from_database import rewrite_base
from read_from_database import take_from_base

def del_row(ID_number : str):
    phone_dic = take_from_base()
    phone_dic.pop(ID_number)
    rewrite_base(phone_dic)