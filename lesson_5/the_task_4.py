"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
from io import TextIOWrapper
Dict_translite = {"one": 'один',
                  "two": 'два',
                  "three": 'три',
                  "four": 'четыре',
                  "five": 'пять',
                  "six": 'шесть',
                  "seven": 'семь',
                  "eight": 'восемь',
                  "nine": 'девять',
                  "ten": 'десять'}
'''чтение из файла и перевод с заменой '''
with open('the_task_4.txt', 'r', encoding='UTF-8') as fail:
    list = [[Dict_translite[el.split(' - ')[0]], el.split(' - ')[1]] for el in fail.readlines()]
"""запись в новый фаил"""
with open('the_task_4_translite.txt', 'w', encoding='UTF-8') as fail_translite:
    for el in list:
        fail_translite.write(f'{el[0]} - {el[1]}')
