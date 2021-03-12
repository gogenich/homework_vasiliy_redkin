'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные
для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.'''
class Warehouse:
    """класс склад """

    """список оргтехники хранящейся на складе"""
    tehnic_list = [{'name': None, 'model': None, 'quantity': None}]

    def __init__(self, name):
        """функция принимает имя склада"""
        self.name = name

    def to_accept(self, equipment, quantity):
        """функция принамает товар на склад (объект оргтехники, колличество)
        так же осуществляеться проверка на правильность введенных данных"""
        try:
            self.equipment = equipment
            self.quantity = int(quantity)
        except ValueError:
            print(f'введите правильное значение колличества {equipment.name} {equipment.model}')
            return
        for el in self.tehnic_list:
            try:
                if el['model'] == equipment.model and el['name'] == equipment.name:
                    el['quantity'] = el['quantity'] + quantity
                    return self.tehnic_list
            except AttributeError:
                print('отсутствует объект оргтехники, введите правильное значение')
                return
        tehnic = equipment.__dict__
        tehnic['name'] = equipment.name
        tehnic['quantity'] = quantity
        self.tehnic_list.append(tehnic)

    @property
    def state(self):
        """проверяет состояние склада"""
        rezult = ''
        for el in self.tehnic_list[1:]:
            rezult = rezult + f'{el} \n'
        print(rezult)

    def broadcast(self, name, model, quantity, dep):
        """осуществляет передачу оргтехники
         в колличестве quantity в указанный депортамент dep"""
        for el in self.tehnic_list:
            if el['model'] == model and el['name'] == name and el['quantity'] >= quantity:
                el['quantity'] = el['quantity'] - quantity
                print(f'{name} модели {model} передан в {dep} в колличестве {quantity} шт')
                return self.tehnic_list
        print('проверьте наличие указанного товара на складе')


class Office_equipment:

    name = ''

    def __init__(self, model, price):
        self.model = model
        try:
            self.price = int(price)
        except ValueError:
            print('цена должна указываться в цифрах')


class Printer(Office_equipment):

    name = 'printer'


class Ckaner(Office_equipment):

    name = 'skaner'


class Cseroks(Office_equipment):

    name = 'Cseroks'


#создаем склад оргтехники
c = Warehouse('склад оргтехники')

# создаем оргтехнику разных моделей(модель, цена за штуку)
s_1 = Ckaner('model_1', 10)
s_2 = Ckaner('model_2', 15)

cse_1 = Cseroks('model_1', 10)
cse_2 = Cseroks('model_2', 35)

p_1 = Printer('model_1', 9)
p_2 = Printer('model_2', 10)

#добавляем технику на склад(вид, колличество)
c.to_accept(p_1, 20)
c.to_accept(cse_1, 30)
c.to_accept(s_1, 10)

#добавляем технику с одинаковыми моделями на склад
c.to_accept(p_1, 1)
c.to_accept(cse_1, 1)
c.to_accept(s_1, 1)

#добавляем технику с разными моделями на склад
c.to_accept(p_2, 3)
c.to_accept(cse_2, 3)
c.to_accept(s_2, 3)

#проверяем наличие техники на складе
#c.state

#допускаем ошибку при добавлении колличества добавляемого товара
#c.to_accept(p_2, 'wewe')

#допускаем ошибку при добавлении обекта
#c.to_accept(1, 10)

#передаем товар
c.broadcast('printer', 'model_2', 1, 'ooo')
#проверяем после передачи
c.state

#проверяем товар после передачи
#c.state

#c.broadcast('printer', 'model_2', 20, 'ooo')
#c.state









