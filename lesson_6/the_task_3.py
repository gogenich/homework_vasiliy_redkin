"""3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""
class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        print(f'Gолное имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        result = self._income['wage'] + self._income['bonus']
        print(f'Доход сотрудника с учетом премии: {result}')

p = Position('Ivan','Ivanov','Driver', {'wage': 10000, 'bonus': 5000})
print(p.name)
print(p.surname)
print(p.position)
p.get_full_name()
p.get_total_income()
