#Создайте класс Круг, который имеет атрибут радиуса и методы  для вычисления площади,
#длины окружности и диаметра
radius1 = int(input("Введите ваше число: "))

class Circle:
    def __init__(self, radius = radius1):
        self.radius = radius

    def Diametr(self):
        self.diametr = self.radius * 2
        print(self.diametr)

    def Ploshad(self):
        self.ploshad = 3.14 * self.radius ** 2
        print(self.ploshad)

    def Dlina(self):
        self.dlina = 3.14 * self.diametr
        print(self.dlina)

Circle1 = Circle()
Circle1.Diametr()
Circle1.Ploshad()
Circle1.Dlina()