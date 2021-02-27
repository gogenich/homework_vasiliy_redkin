"""4. Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""
class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self, speed):
        self.speed = speed
        print(f'машина {self.name} поехала со скоростью {self.speed }')

    def stop(self):
        self.speed = 0
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'машина {self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'тукущая скорость машины {self.name} = {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'тукущая скорость машины {self.name} = {self.speed} ВНИМАНИЕ вы привысили скорость')
        else:
            print(f'тукущая скорость машины {self.name} = {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'тукущая скорость машины {self.name} = {self.speed} ВНИМАНИЕ вы привысили скорость')
        else:
            print(f'тукущая скорость машины {self.name} = {self.speed}')

class PoliceCar(Car):
    pass

boss_car = Car(30, 'red', 'Boss')
tawn_car = TownCar(60,'yelloy', 'Tawn')
sport_car = SportCar(90, 'black', 'Sport')
work_car = WorkCar(30, 'braun', 'work')
police_car = PoliceCar(120, 'ping', 'Polise', True)
#boss_car.go(30)
#boss_car.stop()
#boss_car.go(40)
#boss_car.turn('направо')
#boss_car.turn('налево')
#tawn_car.go(61)
#tawn_car.show_speed()
#tawn_car.stop()
#tawn_car.go(50)
#tawn_car.show_speed()
#tawn_car.stop()
#sport_car.go(120)
#sport_car.show_speed()
#sport_car.stop()
#work_car.go(60)
#work_car.show_speed()
#work_car.stop()
#police_car.go(60)
#police_car.show_speed()
#police_car.stop()