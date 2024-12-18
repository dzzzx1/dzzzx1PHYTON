# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится нуль?

def steps_to_zero(num):
  steps = 0
  while num != 0:
    steps += 1
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

    num -= sum
  print("Количество действий до 0:", steps)

while True:
  try:
    num = int(input("Введите число: "))
    steps_to_zero(num)
  except:
    print("Что то пошло не так")