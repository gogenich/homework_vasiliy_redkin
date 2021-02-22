def my_fanc_1 (x,y):
    rezult = x ** y
    return rezult

def my_fanc_2 (x, y):
    for i in range(1, abs(y)):
        x = x * abs(y)
    rezult = 1 / x
    return rezult



x = float(input('введите действительное положительное число X: '))
y = int(input('введите целое отрицательное число У: '))
print(f'резельтат решения первым способом(my_fanc_1) с помощью **: {my_fanc_1(x, y)}')
print(f'резельтат решения вторым способом(my_fanc_2) с помощью цикла: {my_fanc_2(x, y)}')
