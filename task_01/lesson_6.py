# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего.
# Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.

start_distance = float(input('Start distance: '))
target_distance = float(input('Finish distance: '))

distance_ = start_distance
day_counter = 1

while distance_ < target_distance:
    day_counter += 1
    distance_ *= 1.1

print(day_counter)
