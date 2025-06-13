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
    f1.write('-99 6 12 -36 20 45 100 -15')


with open('1.txt', 'r') as f1:
    data = f1.read().split()
    numbers = list(map(int, data))


count = len(numbers)
average = sum(numbers) / count


new_sequence = []
if count > 0:

    new_sequence.append(numbers[0])


    for i in range(1, count - 1):
        new_val = (numbers[i - 1] + numbers[i + 1]) ** 2
        new_sequence.append(new_val)


    if count > 1:
        new_sequence.append(numbers[-1])


with open('2.txt', 'w', encoding="utf-8") as f2:
    f2.write("Исходные данные:\n")
    f2.write(' '.join(map(str, numbers)) + "\n\n")
    f2.write(f"Количество элементов: {count}\n")
    f2.write(f"Среднее арифметическое элементов: {average}\n\n")
    f2.write("Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов:\n")
    f2.write(' '.join(map(str, new_sequence)))