from random import randint
"""i - колличество эдевенсов в спписке"""
i = 10
"""задаю случайный список с колличеством i"""
list = [randint(1, i) for el in range(i)]
"""генерирую новый список с элементами не имеющих повторений"""
new_list = [ list[i] for i in range(i) if list.count(list[i]) == 1 ]
print(f'случайный список: {list}')
print(f'список с элементами не имеющих повторений: {new_list}')
