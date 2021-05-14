# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def my_func():
    try:
        time = int(input("Выработка в часах: "))
        salary = int(input("Ставка в час: "))
        bonus = int(input("Премия: "))
        res = time * salary + bonus
        print(f'заработная плата сотрудника: {res}')
    except ValueError:
        print('Not a number')


my_func()