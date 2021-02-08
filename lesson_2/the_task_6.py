l = []
namber = int(input('введите колличество товаров: '))
i = 0
while i < namber:
    name = input(f'введите название {i+1} товара: ')
    prise = int(input(f'введите цену {i+1} товара: '))
    quantity = int(input(f'введите колличество {i+1} товара: '))
    unit = input(f'введите единицу измерения {i+1} товара: ')
    s = {"название": name,
         'цена': prise,
         'колличество': quantity,
         'единица измерения': unit}
    t = (i + 1, s)
    l.append(t)
    i = i + 1
print(l)
#naliz = input('введите значение для анализа(название, цена, колличество, единица измерения): ')
#for l_analiz in l:
   # print()
#s_analiz = {analiz: l_analiz}
