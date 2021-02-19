from random import randrange, randint
"""i - колличество эдевенсов в спписке"""
i = 10
"""задаю случайный список с колличеством i"""
list = [randint(1, i) for el in range(i)]
"""генерирую новый список значений с улновем что последущее больше предидущего"""
new_list = [list[i] for i in range(1, i) if list[i] > list[i - 1]]
"""вывод списков"""
print(f'генерируемый список: {list}')
print(f'список с условием, что последущее больше предидущего: {new_list}')