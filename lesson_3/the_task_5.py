
sum = 0
i = True
while i == True:
    nambers = (input('введите числа через пробел либо @ для выхода из функции: '))
    nambers = nambers.split()
    for namber in nambers:
        if namber == "@":
            i = False
        else:
            sum = sum + int(namber)
    print(sum)