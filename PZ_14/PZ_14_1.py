#Из исходного текстового файла (expansion.txt) выбрать имена файлов,
#соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество

import re

f1 = open('expansion.txt', encoding='UTF-8')
f2 = f1.read()
f1.close()

files = re.findall(r'\b[а-яёА-ЯЁa-zA-Z]\w*[.][xlcsmhtpy]+', f2)
print(files)

len = len(files)
print('Количество полученных элементов:', len)