from functools import reduce
"""функция умножения"""
def func_multiplication(old,new):
    return old * new
"""генерирую список от 100 до 1000 с шагом 2"""
list = [el for el in range(100,1000,2)]
print(reduce(func_multiplication, list))