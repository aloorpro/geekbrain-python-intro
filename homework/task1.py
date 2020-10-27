# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
# 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
from itertools import cycle
from time import sleep


class TrafficLight():
    __lights = [('красный', 7),
                ('желтый', 2),
                ('зеленый', 9),
                ('желтый', 2)]

    def __init__(self):
        self.__color = None

    def running(self, total_work=60):
        print("Запускаем светофор")
        when_stop = 0
        self.__running = True
        for light, secs in cycle(TrafficLight.__lights):
            self.color = light
            print(self.color)
            when_stop += secs
            sleep(secs)
            if when_stop >= total_work:
                print("Останавливаем светофор")
                break


if __name__ == '__main__':
    my_tf = TrafficLight()
    try:
        seconds = int(input('Enter secs to work: '))
    except ValueError:
        print("Непонятно")
        seconds = 60
    my_tf.running(seconds)
