# функция проверки ввода целого числа (положительного или отрицательного)

def input_int_return(input_value:str):
    checking_continue = True
    is_minus = False
    count = 1
    while checking_continue:
        value = input(input_value)
        if value[0] == "-":
            value = value.replace("-","")
            is_minus = True
        if value.isdigit():
            number = int(value)
            if is_minus:
                number *= -1
            checking_continue = False
        elif count < 3:
            print("Ввели не число. Попробуйте снова")
            count += 1
        else:
            print("Закрытие программы")
            exit()
    return number
