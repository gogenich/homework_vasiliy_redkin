l = [7, 6, 4, 3, 3, 2]
namber = int(input('введите целое положительное число: '))
print(f'старый список: {l}')
i = 0
for x in l:
    if namber > x:
        l.insert(i, namber)
        break
    i = i + 1
print(f'новый список с введенным числом: {l}')
print(f'позиция введенного числа: {i}')
