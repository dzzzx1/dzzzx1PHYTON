#Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих».
while True:
    num1 = int(input("Введите первое число:"))
    num2 = int(input("Введите второе число:"))
    num3 = int(input("Введите третье число:"))
    if num1 == num2 or num1 == num3 or num2 == num3:
        print(True)
    else:
        print(False)