# Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов
# списка с номерами от K до L включительно.

while True:
    try:
        k = int(input("Введите число K: "))
        if k < 1:
            print("число должно быть больше 1")
            break
        l = int(input("Введите число L: "))
        if l < k:
            print("число должно быть больше", k)
            break
        n = int(input("Введите размер списка: "))
        if n < l:
            print("Значение должно быть больше", l)
            break

        list = []
        for i in range(n):
            a = int(input("Введите элемент списка: "))
            list += [a]
        print(list)

        sum = 0
        for i in range(k, l + 1):
            sum += list[i]
        print("Сумма чисел от K до L:", sum)
    except:
        print("Что то пошло не так")