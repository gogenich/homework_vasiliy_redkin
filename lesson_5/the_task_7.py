"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
from io import TextIOWrapper
import json
with open('the_task_7.txt', 'r', encoding='UTF-8') as fail:
    content = fail.readlines()

profit = {el.split(' ')[0]: int(el.split(' ')[2]) - int(el.split(' ')[3]) for el in content}

average_profit = 0
for el in profit:
    if int(profit[el]) > 0:
        average_profit = average_profit + int(profit[el])

rezult = [profit, {'average_profit': average_profit}]
print(rezult)
with open ('json_fail.json', 'w', encoding='UTF-8') as json_fail:
    json.dump(rezult, json_fail)

