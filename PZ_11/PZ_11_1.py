#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Исходные данные:
#Количество элементов:
#Среднее арифметическое элементов:
#Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
#соседних элементов:


with open('1.txt', 'w') as f1:
    f1.write('-1 6 1 -3 2 4 10 -4')


with open('1.txt', 'r') as f1:
    data = f1.read().split()
    numbers = list(map(int, data))


count = len(numbers)
average = sum(numbers) / count if count > 0 else 0

new_sequence = []
for i in range(count):
    if i == 0:
        if count > 1:
            new_val = numbers[1] ** 2
        else:
            new_val = numbers[0] ** 2
    elif i == count - 1:
        if count > 1:
            new_val = numbers[-2] ** 2
        else:
            new_val = numbers[0] ** 2
    else:
        new_val = (numbers[i - 1] + numbers[i + 1]) ** 2

    new_sequence.append(new_val)


with open('2.txt', 'w', encoding="utf-8") as f2:
    f2.write("Исходные данные:\n")
    f2.write(' '.join(map(str, numbers)) + "\n\n")
    f2.write(f"Количество элементов: {count}\n")
    f2.write(f"Среднее арифметическое элементов: {average}\n\n")
    f2.write("Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов:\n")
    f2.write(' '.join(map(str, new_sequence)))