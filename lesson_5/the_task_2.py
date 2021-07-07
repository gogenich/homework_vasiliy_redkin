"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке."""

from io import TextIOWrapper
with open('the_task_2.txt', 'r', encoding = 'UTF-8') as fail:
    content = fail.readlines()

print(f'клличество строк = {len(content)}')
world = [print(f'колличество слов в {el + 1} строке = {len(content[el].split(" "))}') for el in range(0, len(content))]



