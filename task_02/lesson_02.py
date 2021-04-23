my_list = input('Введите числа через пробел: ').split()
el = 0
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print('Результат:', my_list)
