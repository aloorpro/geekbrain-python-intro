# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
from random import randint

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = bool(is_police)

    def go(self):
        return f"машина {self.name} поехала"

    def stop(self):
        return f"машина {self.name} остановилась"

    def turn(self, direction):
        return f"машина {self.name} повернула направо" \
            if direction else f"машина {self.name} повернула налево"

    def show_speed(self):
        return f"скорость машины {self.name}: {str(self.speed)}"


class TownCar(Car):
    def show_speed(self):
        return f"скорость машины {self.name}: {str(self.speed)}" if self.speed <= 60 else \
            f"скорость машины {self.name}: {str(self.speed)}. Превышено =("


class WorkCar(Car):
    def show_speed(self):
        return f"скорость машины {self.name}:{str(self.speed)}" if self.speed <= 40 else \
            f"скорость машины {self.name}: {str(self.speed)}. Превышено =("


class SportCar(Car):
    """Sport Muscle Car"""


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


name, speed, color = "Машинка", 45, "черный"
for car in [TownCar(name, speed, color),
            WorkCar(name, speed, color),
            SportCar(name, speed, color),
            PoliceCar(name, speed, color)]:
    for i in [car.go(), car.stop(), car.turn(randint(0, 1)), car.show_speed()]:
        print(i)
