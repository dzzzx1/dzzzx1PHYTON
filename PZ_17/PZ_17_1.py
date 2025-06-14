from tkinter import *
import tkinter as tk
from tkinter import ttk


root = Tk()
root.title('Тестовая форма')
root.geometry('300x430')

user_info = LabelFrame(root)
user = LabelFrame(root)
user_info.pack(fill='both', padx=5, pady=5)
user.pack(fill='both', padx=5, pady=5)

user_info_name = Label(user_info, text='Имя')
user_info_name.grid(row=0, column=0, sticky='w', padx=5, pady=5)
input_name = Entry(user_info)
input_name.grid(row=0, column=1, padx=5, pady=5)

user_info_psw = Label(user_info, text='Пароль')
user_info_psw.grid(row=1, column=0, sticky='w', padx=5, pady=5)
input_psw = Entry(user_info)
input_psw.grid(row=1, column=1, padx=5, pady=5)


pol = Label(user_info,text='Выберите пол')
pol.grid(row=2,column=0,sticky='w', padx=5,pady=5)
var1 = IntVar()
button1 = Radiobutton(user_info,text='Мужской',variable=var1,value=1)
button1.grid(row=2,column=1,sticky='w', padx=5,pady=0)
button2 = Radiobutton(user_info,text='Женский',variable=var1,value=2)
button2.grid(row=3,column=1,sticky='w', padx=5,pady=0)

ttk.Label(user_info, text="Континент").grid(row=4, column=0, sticky=tk.W, padx=5,pady=5)
continent = tk.StringVar(value="Евразия")
continent_combo = ttk.Combobox(user_info, textvariable=continent, width=17)
continent_combo['values'] = ("Евразия", "Африка", "Северная Америка", "Южная Америка", "Австралия", "Антарктида")
continent_combo.grid(row=4, column=1, sticky=tk.W, padx=5,pady=5)

var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
my_text = Label(user_info,text='Еда')
my_text.grid(row=5, column=0, sticky='w', padx=5, pady=5)
check = Checkbutton(user_info, text=u'Завтрак', variable=var2,onvalue=1,offvalue=0)
check.grid(row=5, column=1, sticky='w', padx=5, pady=1)
check = Checkbutton(user_info, text=u'Обед', variable=var3,onvalue=1,offvalue=0)
check.grid(row=6, column=1, sticky='w', padx=5, pady=1)
check = Checkbutton(user_info, text=u'Ужин', variable=var4,onvalue=1,offvalue=0)
check.grid(row=7, column=1, sticky='w', padx=5, pady=1)

user_remark = ttk.Label(user_info, text='Замечание')
user_remark.grid(row=8, column=0, sticky='w', padx=5, pady=5)
input_rm = Text(user_info, width=15, height=8)
input_rm.grid(row=8, column=1, padx=0, pady=5)

register_button = ttk.Button(user, text="Отмена")
register_button.pack(side=tk.RIGHT, padx=5)
register_button = ttk.Button(user, text="Отправить")
register_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()