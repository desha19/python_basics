# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить
# на своем месте.
# Для заполнения списка элементов необходимо использовать
# функцию input().

my_list = input('Введите числа через пробел: ').split()
el = 0
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print('Результат:', my_list)
