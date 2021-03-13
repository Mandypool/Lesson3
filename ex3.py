# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.

def my_func(argument_1, argument_2, argument_3):
    if argument_1 >= argument_3 and argument_2 >= argument_3:
        return argument_1 + argument_2
    elif argument_1 > argument_2 and argument_1 < argument_3:
        return argument_1 + argument_3
    else:
        return argument_2 + argument_3


print(f'Сумма введенных наибольших чисел = {my_func(int(input("Введите число 1: ")), int(input("Введите число 2: ")), int(input("Введите число 3: ")))}')