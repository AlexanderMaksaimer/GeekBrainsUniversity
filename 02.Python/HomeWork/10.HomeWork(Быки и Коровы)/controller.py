import random

# Создаем четырезначное число
def create_number() -> int:
    while True:
        num = random.randint(1000, 9999)
        if search_dupli(num):
            return num

#Превращаем число в список
def num_in_list(num: int) -> list:
    return [int(i) for i in str(num)]

#Чек на повтор цифр. Возвращает 'True' если не нашел таких повторов
def search_dupli(num: int) -> bool:
    number_check = num_in_list(num)
    return len(number_check) == len(set(number_check))

# Поиск быков и коров. Проходим по списку
def bulls_and_cows(num: int, guess: int) -> list[int]:
    chickago_bulls_cows = [0, 0]
    number = num_in_list(num)
    move = num_in_list(guess)
    for i, j in zip(number, move):
        if j in number:  # смотрим есть ли цифра в списке
            if j == i:  # Если цифра есть и стоит на нужном месте. Бычок угадан
                chickago_bulls_cows[0] += 1
            else:  # цифра в загаданном числе есть, но не на том месте. Корова поймана
                chickago_bulls_cows[1] += 1
    return chickago_bulls_cows