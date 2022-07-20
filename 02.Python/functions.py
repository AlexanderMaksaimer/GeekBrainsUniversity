import random

def input_number(text):  #функция для проверки что введено число

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else :
            print("Вы ввели не число , попробуйте снова ")
    return coord

def input_number_test_not_minus(text): #функция проверки что введено положительное число

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
            print("Entered number < 0 , took +")
        if coord.isdigit():
            coord = int(coord)
            int_test = False
        else :
            print("Not a number , try again")
    return coord

def input_num_check_float(text): #функция проверки что введено дробное число

    int_check = True
    minus = False
    while int_check:
        coord = input(f"{text}")
        if coord[0] == "-":
            minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if minus:
                coord *= -1
            int_check = False
        elif coord.isdecimal:
            coord = float(coord)
            if minus:
                coord *= -1
            int_check = False
        else :
            print("Not a number , try again")
    return coord

def input_num_check_bigger_zero(text : str) -> int:  # функция ввода числа и проверки что оно больше нуля (0)
    """Check - if input is a integer > 0
    Args:
        text (str): input text - what should be writen before input 
    Returns:
        int: integer number that is > 0
    """
    int_check = True
    minus = False
    while int_check:
        number = input(f"{text}") # ввод числа с описанием
        if number[0] == "-": # проверка числа, что оно <0 
            minus = True
            number = number.replace("-","") # убирает 0 и информирует что число стало положительным 
            print("Entered number < 0 , removed '-' ") 
        if number.isdigit():# если число формата integer - меняет ему тип
            number = int(number)
            if number == 0:
                print("Please, enter number > 0")# если число меньше 0 , не даёт закончить цикл и повторно просит ввести число
            else:
                int_check = False
        else :
            print("Not a number , try again please")
    return number

def array_creation(length_of_array : int , min_for_random : int , max_for_random : int) -> list: 
    # Создание списка из случайных чисел
    """Creation of array with random numbers
    Args:
        length_of_array (int): length of array
        min_for_random (int): minimum number in array
        max_for_random (int): maximum number in array
    Returns:
        list: array of random numbers
    """
    # создаем лист (массив) определенной длинны с рандомом
    list_of_numbers = []
    for i in range(0,length_of_array):
        list_of_numbers.append(random.randint(min_for_random,max_for_random))
    return list_of_numbers

def array_creation_float(length_of_array : int,bit_depth = 10 , round_param = 3) -> list:
    """cration of list with random float numbers
    Args:
        length_of_array (int): length of array
        bit_depth (int, optional): the length of number (digits) 10,100,1000 etc. Defaults to 10.
        round_param (int, optional): to waht ammoutn of numbers to round. Defaults to 3.
    Returns:
        list: _description_
    """
    # создание массива дробных значений и затем перевод их в нужный формат
    list_of_numbers = []
    for i in range(0,length_of_array):
        list_of_numbers.append(round(random.random()*bit_depth,round_param))
    return list_of_numbers

def sum_number_odd_positions(list_of_numbers:list) -> int:
    #функция суммирования элементов массива на нечетных позициях
    """Count sum of elements thet are on not even positions
    Args:
        list_of_numbers (list): array of numbers 
    Returns:
        int: sum of elements at odd positions
    """
    # если индекс не чётный, то увеличиваем сумму на значение под этим индексом
    sum = 0
    index = 0
    for i in list_of_numbers:
        if index % 2 != 0:
            sum += i
        index += 1

    return sum

def not_in_array(list_of_numbers:list) -> str:
    #функция поиска элементов не на каждой позиции
    """Makes a text with elements on not even positions
    Args:
        list_of_numbers (list): array in which not even positions will be looked up
    Returns:
        str: text of elements
    """
    # сначала считаем кол-во элементов для последующей печати
    result = ""
    count = 0
    main_index = 0
    for i in list_of_numbers:
        if main_index % 2 != 0:
            count += 1
        main_index += 1
    index = 0
    
    for i in list_of_numbers: 
        if main_index % 2 != 0:
            index += 1
            result += str(i)
            if index < count: # пока эллемент не последний , добавляет " и "
                result += " и "
        main_index += 1
    return result

def multiplication(list_of_numbers : list) -> list:
    #функция перемножения значений из массива(листа). Например первое и последнее, второе и предпоследнее
    """multiplication of pair in list (for example: 0,-1 / 1,-2)
    Args:
        list_of_numbers (list): array in wich multiplication will ocured
    Returns:
        list: list of multiplied pairs
    """
    # в середине перемножаем первый и последний эллемент, и добавляем результат в новый список
    multi_list = []
    for i in range (0,int(len(list_of_numbers)/2)):
        multi_list.append(list_of_numbers[i] * list_of_numbers[-(i+1)])
    # если кол-во эллементов нечётное, тогда средний эллемент возводим в квадрат
    if len(list_of_numbers) % 2 != 0:
        multi_list.append(list_of_numbers[len(list_of_numbers) % 2+1] ** 2)
    return multi_list



def check_min_max_fractional_numbers(list_of_numbers : list) -> int:
    # функция поиска минимального и максимального значения в списке дробных чисел и поиск разницы в остатках
    """Search min and max value of fraction part in float numbers in array
    Args:
        list_of_numbers (list): array of float numbers
    Returns:
        int: min and max fractional numbers
    """
    # проходим по массиву дробных чисел и проверяем больше максимума - записываем в максимум, меньше минимума - записываем в минимум
    max = list_of_numbers[0] - int(list_of_numbers[0])
    min = list_of_numbers[0] - int(list_of_numbers[0]) 
    for i in list_of_numbers:
        number = i - int(i)
        if number > max:
            max = number
        if number < min:
            min = number
    return min,max


def recode_number(number : int) -> list:
    #функция перевода из десятичного числа в двоичное
    """Recodes number in 2byte code
    Args:
        number (int): number that should be recoded
    Returns:
        list: 2 byte code of number
    """
    remainder = number 
    list_of_recode =[]
    # деление без остатка на 2. Остаток 1 или 0 пойдет в итоговый результат (в обратном порядке)
    # Процесс идет пока остаток больше 1
    while remainder >= 1:
        remainder = number // 2
        list_of_recode.append(number-remainder*2)
        number = remainder
    array_turn(list_of_recode) # разворачиваем список / массив
    return convert_array_to_integer(list_of_recode) # список в число переводим

def array_turn(list_of_numbers : list):
    # функция разворота массива(листа)
    """Array reversal
    Args:
        list_of_numbers (list): array 
    """
    # переворот списка / массива
    for i in range(0,int(len(list_of_numbers)/2)):
        list_of_numbers[i],list_of_numbers[-(1+i)] = list_of_numbers[-(1+i)],list_of_numbers[i]

def convert_array_to_integer(list_of_numbers : list) -> int:
    #функция перевода массива в одно число (может использоваться в дополнение к предыдущей функции с переводом в двоичную систему)
    """converts list (array) of numbers to one integer
    Args:
        list_of_numbers (list): _description_
    Returns:
        int: _description_
    """
    # перевод массива в одну строчку и затем в одно число
    convert = ""
    for i in list_of_numbers:
        convert = convert + str(i)
    return int(convert)

def fibonachi_positive(fib_range : int) -> list: # положительный фибоначи
    #создание положительного фибоначи (с нуля и 1)
    """Create array with positive numbers of fibonachi
    Args:
        fib_range (int): range of fibonacci numbers
    Returns:
        list: positive part of Negafibonachi
    """
    array_fibonachi = [0,1]
    if fib_range > 1:
        for i in range(2,fib_range+1):
            array_fibonachi.append(array_fibonachi[i-1]+array_fibonachi[i-2])
    return array_fibonachi

def fibonachi_negative(fib_range : int) -> list: # отрицательный фибоначи. 
    #создание отрицательного фибоначи
    """Create array with negative numbers of fibonachi
    Args:
        fib_range (int): range of fibonacci numbers
    Returns:
        list: negative part of Negafibonachi
    """
    array_fibonachi = [0,1]
    if fib_range > 1:
        for i in range(2,fib_range+1):
            array_fibonachi.append(array_fibonachi[i-2]-array_fibonachi[i-1])
    return array_fibonachi

def fibonachi_result(fib_range : int) -> list:
    #функция объединения положительного и отрицательного фибоначи
    """Create genaral array with positive and negative numbers of fibonachi
    Args:
        fib_range (int): range of fibonacci 
    Returns:
        list: general array
    """
    positive = fibonachi_positive(fib_range) # создаёт положителный фибоначи
    negative = fibonachi_negative(fib_range) # создаёт отрицательный фибоначи
    array_turn(negative) # разворачиваем минусовой фибоначи при помощи функции разворота массива
    for i in range(1,fib_range+1): # к минусовому массиву добавляем положительный по каждому эллементу
        negative.append(positive[i])
    return negative


def input_number_examination(text_in_input = "Enter number :" , case_def = 0, min_num = 0,max_num=10,bool_is_not_decimal = True):
    #Проверка что введено число
    """Testing if input is a number
    Args:
        text_in_input (str, optional): Text for input. Defaults to "Enter number :".  \n
        case_def (int, optional):   # 0 : "Is it a number",
                                    # 1 : "Enter integer number ",
                                    # 2 : "Enter number > 0",
                                    # 3 : "Enter number between X > number < Y"
                                    Defaults to 0.\n
        min_num (int, optional): If needed test >= . Defaults to 0.\n
        max_num (int, optional): If needed test <=. Defaults to 10.\n
        bool_is_not_decimal (bool, optional): For between min and max shood it be decimal or not  \n
                                            True - number should not be decimal  \n
                                            False - number could be decimal. Defaults to True.\n
    Returns:
        int,float: output could be int or float
    """

    bool_is_number = True

    while bool_is_number:

        bool_si_minus = False
        bool_is_decimal = False

        number = input(f"{text_in_input}")

        if number[0] == "-":
            bool_si_minus = True
            number = number.replace("-","")

        for i in number:
            if i == ".":
                bool_is_decimal = True
                break
        
        if bool_is_decimal:
                whole_part = ""
                digit_part = ""
                for i in number:
                    if i != ".":
                        whole_part += str(i)
                    else:
                        break
                if whole_part.isdigit():
                    for i in number[len(whole_part)+1:]:
                        digit_part += str(i)
                    if digit_part.isdigit():
                        number = whole_part + "." + digit_part
                    number = float(number)
                    bool_is_number = False
        else:
            if number.isdigit():
                number = int(number)
                bool_is_number = False

        if bool_is_number:
            print("Not a number , try again")
            continue

        if bool_si_minus:
            number *= -1
        
        bool_is_number = input_number_params(number,case_def, min_num,max_num,bool_is_not_decimal)

    return number

def input_number_params(number , case_def, min_num ,max_num,bool_is_not_decimal):
    """Check variants of input input_number_examination
    Args:
        number (_type_): number to check
        case_def (_type_):  # 0 : "Is it a number",
                            # 1 : "Enter integer number ",
                            # 2 : "Enter number > 0",
                            # 3 : "Enter number between X > number < Y",
        min_num (_type_): number >=
        max_num (_type_): number <=
        bool_is_not_decimal (_type_):   True - dont allow decimals
                                        False - allow decimals
    """

            # 0 : "Is it a number",
            # 1 : "Enter integer number ",
            # 2 : "Enter number > 0",
            # 3 : "Enter number between X > number < Y",

    float_bool = True

    if case_def < 0 or case_def > 4:
        print("Wrong argument for test. Need from 0 to 3")
        return True

    match case_def:
        case 0:
            try:
                float(number)
                return False
            except ValueError:
                return True
        case 1:
            for i in str(number):
                    if i == ".":
                        print("Not an integer")
                        float_bool = False
            if float_bool:
                    return False
            else:
                    return True
        case 2:
            if number >= 0:
                return False
            else:
                print("Not >= 0")
                return True
        case 3:
            if bool_is_not_decimal:
                for i in str(number):
                    if i == ".":
                        print("Not an integer")
                        float_bool = False
                if float_bool:
                    if min_num > max_num:
                        min_num,max_num = max_num,min_num
                    if number >= min_num and number <= max_num:
                        return False
                    else:
                        print(f"not >={min_num} or =<{max_num} ")
                        return True
                else:
                    print("Enter not decimal")
                    return True
            else:
                if min_num > max_num:
                    min_num,max_num = max_num,min_num
                if number >= min_num and number <= max_num:
                    return False
                else:
                    print(f"not >={min_num} or =<{max_num} ")
                    return True

def array_creation_random_int(array_length = 10,min_random = 0,max_random = 10) -> list:
    # создание массива определенного количества
    """Creat an array of numbers in range
    Args:
        array_length (int, optional): length of array . Defaults to 10.
        min_random (int, optional): min umber of random. Defaults to 0.
        max_random (int, optional): max number of random. Defaults to 10.
    Returns:
        list: list of int random numbers
    """
    if array_length <=0:
        print("Wrong array length choose , settin it to deffoult 10")
        array_length = 10
    if min_random > max_random:
        print("Min value for random is bigger then max, changing placec")
        min_random,max_random=max_random,min_random
    elif min_random == max_random:
        print("Min = Max values for random - it will be 1 number")

    list_of_numbers =[]
    for i in range(0,array_length):
        list_of_numbers.append(random.randint(min_random,max_random))
    return list_of_numbers

def array_creation_range(range_start=0,range_end=10,range_step=1) -> list:
   #создание массива определенного диапазона
    """Creat a list of numbers in range
    Args:
        range_start (int, optional): Start of range. Defaults to 0.
        range_end (int, optional): end of range (has +1 in formula ). Defaults to 10.
        range_step (int, optional): step of range. Defaults to 1.
    Returns:
        list: list of integer numbers in rage
    """
    if range_start >= range_end:
        print("Start of array is bigger then End, changing placec")
        range_start,range_end = range_end,range_start
    if range_step <= 0:
        print("Wrong step , changing to deffoult 1")
        range_step = 1
    
    list_of_numbers =[*range(range_start,range_end+1,range_step)]
    return list_of_numbers

def array_creation_random_float(array_length = 10,digit_choose = 1,round_digit = 4) -> list:
    #создание массива с рандомными дробными числами
    if digit_choose <0 or digit_choose>9:
        print("Wrong digit choose , settin it to deffoult 1")
        digit_choose = 1
    if round_digit < 0:
        print("Wrong round choose , settin it to deffoult 4")
        digit_choose = 1
    if array_length <=0:
        print("Wrong array length choose , settin it to deffoult 10")
        array_length = 10

    digit_lib = \
        {
            0 : 1 ,
            1 : 10 ,
            2 : 10**2 ,
            3 : 10**3 ,
            4 : 10**4 ,
            5 : 10**5 ,
            6 : 10**6 ,
            7 : 10**7 ,
            8 : 10**8 ,
            9 : 10**9 
        }

    list_of_numbers =[]
    for i in range(0,array_length):
        if round_digit == 0:
            list_of_numbers.append(int(round(random.random()*digit_lib[digit_choose])))
        else:
            list_of_numbers.append(round(random.random()*digit_lib[digit_choose],round_digit))
    return list_of_numbers

def print_dictionary_in_lines(dictionary_array):
    #печать словаря в массиве
    for i in dictionary_array:
        print(f"{i} : {dictionary_array[i]}")

