# Ввести 4 числа. Найти и вывести на экран количество четных чисел.
even_count = 0
for i in range(4):
    while True:
        try:
            num = int(input("Введите число: "))
            if num % 2 == 0:
                even_count += 1
            break
        except :
            print("Что то пошло не так.")

print("Количество четных чисел:", even_count)