# Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
# функции
def rectangle_per(len, wid):
    perimeter = 2 * (len + wid)
    return perimeter


def rectangle_sq(len, wid):
    square = len * wid
    return square


len = int(input("Введите длину прямоугольника: "))
wid = int(input("Введите ширину прямоугольника:"))
print("Периметер прямоугольника:", rectangle_per(len, wid))
print("Площадь прямоугольника:", rectangle_sq(len, wid))
