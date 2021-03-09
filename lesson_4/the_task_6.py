from itertools import count, cycle
from time import sleep
i = 0
namb = int(input('Введите целое число от 0 до 10: '))
"""интератор count"""
for el in count(namb):
    print(el)
    sleep(1)
    if el == 10:
        break

list = input('введите данные списка через пробел: ')
"""интератор cycle"""
for el in cycle(list.split()):
    print(el)
    sleep(1)
    i = i + 1
    if i == 10:
        break