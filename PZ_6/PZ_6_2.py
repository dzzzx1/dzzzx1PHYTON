# Дан целочисленный список размера N. Найти количество различных элементов в
# данном списке.

while True:
    try:
        n = int(input("Введите размер списка: "))
        if n < 1:
            print("Ошибка: введено некорректное значение")
            break

        list = []
        for i in range(n):
            a = int(input("Введите элемент списка: "))
            list += [a]
        print(list)

        list = set(list)
        print("Количество различных элементов:", len(list))
    except:
        print("Что то пошло не так")