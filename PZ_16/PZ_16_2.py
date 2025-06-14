# Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоциклы"
# В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колёс, а классы
# наследники будут иметь свои уникальные свойства и методы.

class Transport:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed


class Car(Transport):
    def __init__(self, wheels, max_speed, color, seats):
        super().__init__(wheels, max_speed)
        self.color = color
        self.seats = seats
    def Characteristics(self):
        print(f'Максимальная скорость: {self.max_speed} км/ч')
        print(f'Количество колёс: {self.wheels} шт')
        print(f'Цвет: {self.color}')
        print(f'Количество мест: {self.seats}')
    def Info(self):
        print(f'Машина цвета {self.color} едет')

class Motorbike(Transport):
    def __init__(self, wheels, max_speed,helmet_color, price):
        super().__init__(wheels, max_speed)
        self.helmet_color = helmet_color
        self.price = price
    def Characteristics(self):
        print(f'Максимальная скорость: {self.max_speed} км/ч')
        print(f'Количество колёс: {self.wheels} шт')
        print(f'Цвет шлема: {self.helmet_color}')
        print(f'Цена: {self.price} к.')
    def Info(self):
        print(f'У водителя мотоцикла цвет шлема {self.helmet_color}')


car = Car(4, 270, "Kрасный" , 5)
car.Characteristics()
car.Info()

print('\n')

motorbike = Motorbike(2, 150, "Чёрный" , 200)
motorbike.Characteristics()
motorbike.Info()