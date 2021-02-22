def my_func(nambers):
    """считаем сумму введенных чисел, а так же проверяем на наличие символа для выхода"""
    sum = 0
    for namber in nambers:
        if namber == "@":
            global I
            I = False
        else:
            sum = sum + int(namber)
    return sum

I = True
while I == True:
    nambers = (input('введите числа через пробел либо @ для выхода из функции: '))
    nambers = nambers.split()
    print(f'сумма введенных чисел равна: {my_func(nambers)}')


