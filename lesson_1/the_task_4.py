namber = int(input('введите целое положительное число: '))
max = 0
while namber != 0:
    numeral = namber % 10
    if numeral > max:
        max = numeral
    namber = int(namber / 10)
print(max)
