# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint

__dict_result = {}
__all__ = ['find_number', 'my_zagadka_dict', 'my_zagadka', 'output_dict_result']


def find_number(a: int, b:int , popit:int ) -> bool:
    number = randint(a, b)
    while popit:
        our_number = int(input('Введти новое число: '))
        if our_number == number:
            return True
        elif our_number > number:
            print('Наше число больше чем угадываемое число.')
        else:
            print('Наше число меньше чем угадываемое число.')
        popit -= 1
    return False


def my_zagadka(zagadka, variant, attemts):
    for i in range(attemts):
        print('загадка: ', zagadka)
        otvet = input('введите ответ: ')
        if otvet in variant:
            print('верно')
            print(f'загадка "{zagadka}" угадана с {i + 1} попытки')
            return i + 1


        else:
            print(f'неверно, осталось {attemts - i - 1} попыток')
    print('попытки кончились')
    return 0


# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


def my_zagadka_dict():
    dict_zagatka = {
        'что синего цвета': ['небо', 'море', 'цветок'],
        'города России': ['Питер', 'Москва', 'Воронеж'],
        'типы данных': ['строка', 'список', 'кортеж']
    }
    for key, value in dict_zagatka.items():
        __dict_result[key] = my_zagadka(key, value, 3)

    return 0


def output_dict_result():
    for key, value in __dict_result.items():
        print(f"Загадка: {key}. Была решена за {value} попыток")
