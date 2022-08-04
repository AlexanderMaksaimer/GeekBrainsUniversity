from methods import input_int_return as check

# Начало
def description ():
    print ('\nТелефонный справочник позволяет добавлять, редактировать и удалять контакты')

# Спрашиваем имя пользователя
def hello ():
    user_name = input('\nДоброго времени суток. Напишите ваше имя: ')
    print(f'\nЗдравствуйте, {user_name}!')
    return user_name

# выбор опций
def input_options ( var_0 = '\nЧто собираетесь выполнить? Найти контакт [1],  Добавить информацию [2] или Другая работа со справочником [3]: ',
                    var_1 = 'Поиск контакта для просмотра и редактирования.\n',
                    var_2 = 'Добавление нового контакта в справочник.\n',
                    var_3 = 'Работа со справочником.\n'):
    count = 0
    while count < 3:
        option_value = check(var_0)
        if option_value == 1:
            print (var_1)
            break
        elif option_value == 2:
            print (var_2)
            break
        elif option_value == 3:
            print (var_3)
            break
        else:
            print(f'Некорректное значение. У вас осталось {3-count} попыток')
            count +=1
    return option_value

# Выбор как искать контакт
def search_var ( var_0 = '\nЧерез какой параметр ищем контакт? Имя [1],  Имя + Фамилия [2] Номер телефона [3]: ',
                    var_1 = 'Поиск контакта по Имени.\n',
                    var_2 = 'Поиск контакта по Имени + Фамилии.\n',
                    var_3 = 'Поиск контакта по номеру телефона.\n'):
    count = 0
    while count < 3:
        option_value = check(var_0)
        if option_value == 1:
            print (var_1)
            break
        elif option_value == 2:
            print (var_2)
            break
        elif option_value == 3:
            print (var_3)
            break
        else:
            print(f'Некорректное значение. У вас осталось {3-count} попыток')
            count +=1
    return option_value

# Выбираем опцию, когда нашли контакт: Добавить новый контакт или Работа с данными
def options_find_contact ( var_0 = 'Нашли контакт. Дальнейшие действия? Просмотреть [1],  Редактировать [2] или Удалить [3]: ',
                                var_1 = 'Просмотреть информацию о контакте.\n',
                                var_2 = 'Внести изменения.\n',
                                var_3 = 'Удалить.\n'):
    count = 0
    while count < 3:
        option_value = check(var_0)
        if option_value == 1:
            print (var_1)
            break
        elif option_value == 2:
            print (var_2)
            break
        elif option_value == 3:
            print (var_3)
            break
        else:
            print(f'Некорректное значение. У вас осталось {3-count} попыток')
            count +=1
    return option_value

# Спрашиваем о завершении работы программы или о новом действии. Если выбрано Завершение, в дальнейшем следует завершить
# программу.
def finish (var_0 = 'Вы закончили работу со справочником? Да, завершить работу [1] или Нет, я хочу поработать еще [2]: ',
                        var_1 = 'Завершение работы. Выход из программы.\n',
                        var_2 = 'Продолжаем работу.\n',
                        user_name = ""):
    count = 0
    while count < 3:
        option_value = check(var_0)
        if option_value == 1:
            print (var_1)
            chao_cacao (user_name)
            break
        elif option_value == 2:
            break
        else:
            print(f'Некорректное значение. У вас осталось {3-count} попыток')
            count +=1
    return option_value

def chao_cacao (user_name):
    return print(f'Всего доброго, {user_name}!')