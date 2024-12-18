# Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
# результата предусмотреть в основной программе. Расчет суммы цифр оформить в
# функции

def sum_digit(num):
  while num != 0:
    num1 = num
    x = 0
    while num1 > 0 and num1 % 10 != 0:
      x += 1 # значность числа
      num1 //= 10

    num2 = num
    sum = 0 # сумма цифр
    for i in range(x):
      sum += num2 % 10
      num2 //= 10
    return sum

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

sum1 = sum_digit(num1)
sum2 = sum_digit(num2)
sum3 = sum_digit(num3)

if sum1 >= sum2 and sum1 >= sum3:
  print("Наибольшая сумма цифр у числа" , num1 )
elif sum2 >= sum1 and sum2 >= sum3:
  print(f"Наибольшая сумма цифр у числа" , num2 )
else:
  print(f"Наибольшая сумма цифр у числа" , num3 )