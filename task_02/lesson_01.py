# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

different = ['abc', 123, 1.5, True, [1, 2, 3]]  # Создаём список
for element in different:   # Воспользуемся циклом for для обработки каждого элемента в списке
    print(type(element))    # Спомощью функцию type() проверяем каждый элемент в списке и выводим результат
