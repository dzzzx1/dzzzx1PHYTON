# Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1)
n = int(input("Введите n (n > 1): "))
if n <= 1:
    print("n должно быть больше 1")
else:
    s = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        s += fact
    print("Сумма факториалов:", s)