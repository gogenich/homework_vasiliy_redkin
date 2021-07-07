"""1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:

    def __init__(self, matriks):
        self.matriks = matriks


    def __str__(self):
        rezult = ''
        for el in self.matriks:
            rezult = str(rezult) + '\n' + str(el)
        return f'объект матрица {rezult}'

    def __add__(self, other):
        new_rezult = []
        for j in range(len(self.matriks)):
            rezult = [self.matriks[j][i] + other.matriks[j][i] for i in range(0, len(self.matriks[j]))]
            new_rezult.append(rezult)
        return Matrix(new_rezult)


one = Matrix([[1, 2, 3], [4, 5, 6]])
print(one)
too = Matrix([[3, 5, 6], [6, 7, 8]])
print(too)
rezult = one + too
print(rezult)
