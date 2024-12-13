# Ввести N чисел. Посчитать и вывести количество чисел равных нулю.
n = int(input("Введите количество чисел N: "))
zero_count = 0
for i in range(n):
    while True:
        try:
            num = float(input(f"Введите число: "))
            if num == 0.0:
                zero_count += 1
            break
        except:
            print("Что то пошло не так.")

print("Количество нулей:", zero_count)