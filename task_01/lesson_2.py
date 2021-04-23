seconds = int(input('Введите колличество секунд: '))
hours = seconds // 3600
minutes = seconds // 60 % 60
residue_seconds = seconds % 60
print('{:02}:{:02}:{:02}'.format(hours, minutes, residue_seconds))
