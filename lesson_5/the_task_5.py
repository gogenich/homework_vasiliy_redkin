"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран."""
from io import TextIOWrapper
"""создали фаил и записали в него числа"""
with open('the_task_5.txt', 'w', encoding='UTF-8') as fail:
    fail.write('1 2 3 4 5 6')
"""прочитали фаил и сложили числа"""
with open('the_task_5.txt', 'r', encoding='UTF-8') as fail:
    sum = 0
    for el in fail.readline().split(' '):
        sum = sum + int(el)

print(sum)