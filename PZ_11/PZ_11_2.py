# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.

punctuation_count = 0
lines = []


with open('text18-18.txt', encoding='UTF-16') as f:
    for i, line in enumerate(f):

        lines.append(line)


        print(line, end='')


        if i < 4:
            for char in line:

                if char in '.,!?;:"\'()-...—':
                    punctuation_count += 1

print(f'\nКоличество знаков пунктуации в первых четырех строках: {punctuation_count}')

# Формируем новый файл с обратным порядком строк
with open('text18-18-2.txt', 'w', encoding="utf-8") as f_out:
    # Реверсируем порядок строк
    reversed_lines = reversed(lines)
    f_out.writelines(reversed_lines)