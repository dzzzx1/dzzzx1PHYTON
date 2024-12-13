# Дано вещественное число X и целое число N (> 0). Найти значение выражения
# X -X^3/(3!) + X^5/(5!) - ... + (-1)^N-X^2-N+1 /((2-N+1)!) (N! = 12 ...N).
# Полученное число является приближенным значением функции sin в точке X.
x = float(input("Введите вещественное число X: "))
n = int(input("Введите целое число N (> 0): "))
if n <= 0:
    print("Число должно быть больше нуля!")
else:
    total_sum = 0
    for i in range(1, n + 1):
        num = (-1)**(i - 1) * (x**(2 * i - 1))
        num1 = 1
        for j in range(1, 2 * i):
            num1 *= j
        total_sum += num / num1
    print("Приближенное значение sin(x):", total_sum)