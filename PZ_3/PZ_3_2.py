#Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений,
# а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B.
a = int(input("Введите переменную А: "))
b = int(input("Введите переменную B: "))
if a != b:
    new_a = a+b
    new_b = a+b
    print("новые значения:", new_a, new_b)
else:
    a = 0
    b = 0
    print("новые значения:", a, b)