# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

print('Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах')

def text_split(text: str) -> str :
    """ Делим символы пробелом
    Args:
        text (str): ввод текста для RLE
    Returns:
        str: Выводятся все символы через пробел
    """
    result = f"{text[0]}"
    for i,item in enumerate(text[1:]):
        if item != text[i]:
            result += " " + item
        else:
            result += item
    result_list = result.split()
    return result_list

def RLE(list_str: str) -> str:
    """Строку с пробелами делим и считаем количество символов
    Args:
        list_str (str): строка с пробелами
    Returns:
        str: код REL
    """
    result = ""
    for i in list_str:
        result += f"{len(i)}{i[0]}"
    return result

def RLE_str(REL_text: str) -> str:
    """Число + Символ повторяем символ указанное количество раз
    Args:
        REL_text (str): код RLE
    Returns:
        str: Текст
    """
    RLE_list = []
    for i in range(0,len(REL_text),2):
        RLE_list.append([REL_text[i],REL_text[i+1]])
    result = ""
    for i in RLE_list: # тут я хотел в одну строчку сделать чреез *  - но он не захотел , пришлось делать цикл 
        for j in range(0,int(i[0])):
            result += i[1]
    return result

def file_create(path : str,text : str):
    """Создание файла с текстом
    Args:
        path (str): Название и путь к файлу
        text (str): текст для записи
    """
    file = open(path , "w",encoding='utf-8')
    file.write(text)
    file.close()

def file_read(path : str) -> str:
    """Чтение файла и возврат строки
    Args:
        path (str): название и путь к файлу
    Returns:
        str: возвращение строки
    """
    file = open(path , "r",encoding='utf-8')
    data = file.read()
    return data

file_name = "text"
file_format = "txt"
file_path = file_name+"."+file_format

str_text = "oooooooohhhhhhhhmmmmmmmllllllliiii1111119999990000"

file_create(file_path,str_text) 
text_line = file_read(file_path)

file_name = "RLE_test_text"
file_path = file_name+"."+file_format
file_create(file_path,RLE(text_split(text_line)))
RLE_code_text = file_read(file_path)

file_name = "text_from_RLE"
file_path = file_name+"."+file_format
file_create(file_path,RLE_str(RLE_code_text)) 