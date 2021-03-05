"""2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property"""
from abc import abstractmethod

class Clothes:


    @abstractmethod
    def payment(self):
        pass

    def __add__(self, other):
        rezult = self.payment + other.payment
        return rezult


class Coat(Clothes):


    def __init__(self, v):
        self.v = v

    @property
    def payment(self):
        rezult = round(((self.v / 6.5) + 0.5), 2)
        return rezult


class Costume(Clothes):


    def __init__(self, h):
        self.h = h

    @property
    def payment(self):
        rezult = round(((self.h * 2) + 0.3), 2)
        return rezult


r = Coat(10)
print(r.payment)
e = Costume(10)
print(e.payment)
print(e + r)
