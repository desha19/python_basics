# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369

user_input_number = input('Введите число: ')

if not user_input_number.isdigit():
    print('Число введено не верно')
    exit()

i = 0
for element in range(1, 4):
    i += int(user_input_number * element)
print(i)
