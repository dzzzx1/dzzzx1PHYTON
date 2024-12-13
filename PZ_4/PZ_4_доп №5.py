# Ввести N чисел. Найти и вывести их среднее арифметическое.
n = int(input("Введите количество чисел N: "))
total_sum = 0
for i in range(n):
    while True:
        try:
            num = int(input("Введите число: "))
            total_sum += num
            break
        except:
            print("Что то пошло не так.")

average = total_sum / n
print("Среднее арифметическое:", average)