# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


name = input('enter name: ')
surname = input('enter surname: ')
year = input('enter year: ')
city = input('enter city: ')
email = input('enter email: ')
telephone = input('input telephone: ')

print(my_func(name, surname, year, city, email, telephone))
