# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, num):
        self.size = num

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 64:
            self.__size = 64
        else:
            self.__size = size

    def cloth(self):
        return round(self.size / 6.5 + 0.5, 3)


class Suit(Clothes):
    def __init__(self, num):
        self.height = num

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1.40:
            self.__height = 1.40
        elif height > 2.04:
            self.__height = 2.04
        else:
            self.__height = height

    def cloth(self):
        return round(self.height * 2 + 0.3, 3)


my_coat = Coat(50)
my_suit = Suit(1.8)
print(f'{my_coat.cloth()} + {my_suit.cloth()} = {my_suit.cloth() + my_coat.cloth()}')
