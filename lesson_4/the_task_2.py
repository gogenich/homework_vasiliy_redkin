from random import randrange, randint
"""задаю случайный список"""
list = [randint(1, 10) for el in range(10)]
"""генерирую новый списов с условием что """
new_list = [y for y in list if  < y]
print(list)
print(new_list)