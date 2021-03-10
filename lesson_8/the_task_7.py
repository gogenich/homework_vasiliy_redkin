"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата."""
class Complex_numbers:


    def __init__(self, x, y_i):
        try:
            self.x = int(x)
            self.y_i = int(y_i)
        except ValueError as arr:
            print(f'{arr}x и у должны быть числами')

    def __str__(self):
        return f'{self.x} + {self.y_i}i'

    def __add__(self, other):
        x = self.x + other.x
        y_i = self.y_i + other.y_i
        return Complex_numbers(x, y_i)

    def __mul__(self, other):
        x = (self.x * other.x) + (self.y_i * other.y_i)
        y_i = (self.x * other.y_i) + (self.y_i * other.x)
        return Complex_numbers(x, y_i)



z = Complex_numbers(1, 2)
z_2 = Complex_numbers(3, 4)
print(z)
print(z_2)
rezult = z * z_2
print(rezult)
