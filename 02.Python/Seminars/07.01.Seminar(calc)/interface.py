from methods import check_value_is_digit_and_return_it as check

# Вступление: краткое описание программы
def description ():
    return print ('\nДанная программа может производить простые арифметические действия с комплексными и рациональными числами')

# Спрашиваем имя пользователя и приветствуем его
def say_hello ():
    user_name = input('Представьтесь, пожалуйста. Напишите ваше имя: ')
    print(f'Здравствуйте, {user_name}!')

# Выбираем опцию
def input_options (
                    opt_inquiry = 'Итак, с какими числами будем работать? Комплексные [1] или Рациональные [2]: ',
                    opt_1 = 'Что ж, будем оперировать комплексными числами.\n',
                    opt_2 = 'Значит будем калькулировать рациональные числа.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value

description()
say_hello()
input_options()