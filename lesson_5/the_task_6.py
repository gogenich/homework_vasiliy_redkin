"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все
типы занятий. Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

from io import TextIOWrapper
with open('the_task_6.txt', 'r', encoding='UTF-8') as fail:
    content = fail.readlines()
'''вычленяем название предмета'''
key = [el.split(':')[0] for el in content]
"""вычленяем количество часов"""
valum = []
for el in content:
    rezult = el.split(':')[1]
    rezult = rezult.split(' ')
    sum = 0
    for el in rezult[1:]:
        rezult = el.split('(')[0]
        if rezult == '-':
            rezult = 0
        sum = int(rezult) + sum
    valum.append(sum)
"""генерикуем результат в виде словаря"""
rezult_dict = {key[el]: valum[el] for el in range(0, len(key))}
print(rezult_dict)

