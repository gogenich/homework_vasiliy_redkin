
def my_func (a: int, b: int, c: int):
    """функция котороая принимает 3 параметра и высчитывает
    сумму двух наибольших значений"""
    rezult = a + b + c - min(a, b, c)
    return rezult

a = int(input('введите значение а: '))
b = int(input('введите значение b: '))
c = int(input('введите значение c: '))

print(my_func(a, b, c))