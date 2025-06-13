# Составить генератор (yield), который преобразует все буквенные символы в
# строчные.

text = 'TRUBODUR 899007 dEFgRjK'
def zadanie(a):
    b = a.split()
    yield from [i.lower() for i in b]
lower_text = zadanie(text)
for i in lower_text:
    print(i)