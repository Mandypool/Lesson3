# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(my_func(surname='Oleg', name='Olegov', year='1999', city='Olegcity', email='oleg@mail.ru',
              phone='8-999-888-77-66'))