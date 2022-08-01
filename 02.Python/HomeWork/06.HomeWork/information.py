# Полезная информация
# Допустим, у вас есть функция.
# def is_int(input_number:str):
# '''
# Проверяет аргумент на принадлежность к int
# params:input_number - введенное значение
# return: int или False
# '''
# try:
# input_number = int(input_number)
# return input_number
# except ValueError:
# return False
# Вы можете использовать эту функцию в лямбде. Делается это, примерно, вот так:
# ┌────────────────────────────┐
# │lambda input_number: is_int(input_number) │
# └────────────────────────────┘
# или даже необязательно называть это input_number:
# ┌────────────────┐
# │lambda char: is_int(char)│
# └────────────────┘