#Проверить истинность высказывания:
#«Среди трех данных целых чисел есть хотя бы одна пара совпадающих». ПЗ_3_1

import tkinter as tk

def check_duplicate():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())

        result = num1 == num2 or num1 == num3 or num2 == num3
        result_label.config(text=str(result))

    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа во все поля")
        result_label.config(text="Ошибка")



root = tk.Tk()
root.title("Проверка совпадений")
root.geometry("300x200")


tk.Label(root, text="Первое число:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)


tk.Label(root, text="Второе число:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)


tk.Label(root, text="Третье число:").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)


check_button = tk.Button(root, text="Проверить", command=check_duplicate)
check_button.grid(row=3, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()