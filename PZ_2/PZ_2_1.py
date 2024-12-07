#Вариант 19: Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число.
num = int(input("Введите трехзначное число: "))
num_str = str(num)
if len(num_str) != 3:
  print("число должно быть трехзначным!!")
else:
  try:
    new_num_str = num_str[-1] + num_str[:-1]
    new_num = int(new_num_str)
    print("Полученное число:", new_num)
  except:
    print("Что-то пошло не так")