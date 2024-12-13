negative_count = 0
total_sum = 0
for i in range(4):
    while True:
        try:
            num = float(input("Введите число: "))
            if num < 0:
                negative_count += 1
            total_sum += num
            break
        except:
            print("Что то пошло не так.")

print("Сумма чисел:", total_sum)
print("Количество отрицательных чисел:", negative_count)