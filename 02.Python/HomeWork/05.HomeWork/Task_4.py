# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def spliting_text(text: str) -> str :
    """У меня почему то долго не получалось в пару действий посчитать и схранить символ - пришлось делить все символы пробелом
    Args:
        text (str): вводится текс для RLE кодировки
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

def RLE_code(list_str: str) -> str:
    """По сути - берёт строку с пробелами - дели её и считает кол-во символов
    Args:
        list_str (str): строка с пробелами
    Returns:
        str: код REL
    """
    result = ""
    for i in list_str:
        result += f"{len(i)}{i[0]}"
    return result

def RLE_in_string(REL_text: str) -> str:
    """Берёт пару Число + Символ и поторяет символ указанное кол-во раз
    Args:
        REL_text (str): КОД RLE
    Returns:
        str: Текс
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
    """Созадёт файл с текстом
    Args:
        path (str): Название/Путь_файла
        text (str): текст для записи
    """
    file = open(path , "w",encoding='utf-8')
    file.write(text)
    file.close()

def file_read(path : str) -> str:
    """Читает файл и возвращает строку
    Args:
        path (str): Название/Путь файла
    Returns:
        str: возвращает строку
    """
    file = open(path , "r",encoding='utf-8')
    data = file.read()
    return data

file_name = "text"
file_format = "txt"
file_path = file_name+"."+file_format

str_text = "aaaaaaaawwwwwaaaaaabbbbababaaaaaawwwww111122223333"

# много топорной работы - но хочу сосредоточится на более сложных задачах
# Можно было бы вывести переименовыванеие файлов в лямду или в функии, но мне с ними нужно попрактиковаться, что бы понять

file_create(file_path,str_text) # делает изначально файл с текстом ( в релаьной жизни - файл будет)
line_of_text = file_read(file_path)

file_name = "REL_text"
file_path = file_name+"."+file_format
file_create(file_path,RLE_code(spliting_text(line_of_text))) # То что считал до этого - перевёл в КОД и записал в новый файл
RLE_code_text = file_read(file_path)

file_name = "text_from_RLE"
file_path = file_name+"."+file_format
file_create(file_path,RLE_in_string(RLE_code_text)) # Код с файла - переводит в строку и записывает в новый файл 