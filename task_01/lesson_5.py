# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Enter proceeds: "))
costs = float(input("Enter costs: "))

if proceeds > costs:
    print('Good Job')
    income = proceeds - costs
    print('Profitability of firm {:%}'.format(income / proceeds))
    employees = int(input('Employees string: '))
    print(f'Profitability of employ {income / employees} $')
else:
    print('Bad Job')
