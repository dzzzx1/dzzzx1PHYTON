# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря
avto = {
    "Toyota": ["Corolla", "Camry", "Rav4"],
    "BMW": ["X5", "X6", "X7"],
    "Audi": ["e-tron", "A7", "Q5"]
}

print("Вторые модели:")
for marka in avto:
    model = avto[marka][1]
    print(marka+ ":", model)
print("Все модели:")
for marka, modeli in avto.items():
    print(marka + ": " + modeli[0] + ", " + modeli[1] + ", " + modeli[2])