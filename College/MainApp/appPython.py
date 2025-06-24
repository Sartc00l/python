# импорт tkinter, меню. ttk нужен для Listbox
import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class Item:
    """
    Класс для описания предметов вообще.
    Есть два параметра: название и цена
    """
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price


class InventoryItem(Item):
    """
    Класс для описания вещей в инвентаре. Наследует свойства от
    класса Item. Добавлен третий параметр - количество
    """
    def __init__(self, name=None, price=None, kolichestvo=None):
        super().__init__(name, price)
        self.kolichestvo = kolichestvo


class App:
    def __init__(self):
        # inv_items - список предметов в инвентаре
        self.inv_items = ["Яблоки", "Руда", "Железный меч"]

        self.win = tk.Tk()
        self.win.geometry("800x400+10+10")
        self.win.title("Магазин.Продажа")
        self.setUI() #функция отвечающая за создание интерфейса
        self.win.mainloop()

    def settings_window(self):
        """
        Метод, который создает окно с настройками
        """
        self.set_win = tk.Tk()
        self.set_win.geometry("300x300+810+10")
        self.set_win.title("Настройки")

        def add_item():
            name=name_entry.get()
            pass

        tk.Label(text="Название").pack()
        name_entry=tk.Entry()
        name_entry.pack()
        tk.Label(text="Количество").pack()
        q_entry=tk.Entry()
        q_entry.pack()
        tk.Label(text="Цена").pack()
        price_entry=tk.Entry()
        price_entry.pack()
        tk.Button(text="добавить", command=add_item).pack()

        self.set_win.mainloop()

    def setUI(self):
        # переменная для задания отступов
        p = {'padx': 10, 'pady': 10}
        # переменная для задания шрифта
        font = {'font': ('Helvetica', 16)}
        # подпись к выпадающему списку
        self.name_label = ttk.Label(text="Название", **font)
        # создание выпадающего списка
        items = tk.StringVar()
        self.item_list = ttk.Combobox(textvariable=items)
        # размещение подписи и выпадающего списка
        self.item_list.grid(row=0, column=0, **p)
        self.name_label.grid(row=0, column=1, **p)
        # создание и размещение элементов, отвечающих за количество
        self.q_label = ttk.Label(text="Количество")
        self.q_entry = ttk.Entry()
        self.q_entry.grid(row=1, column=0, **p)
        self.q_label.grid(row=1, column=1, **p)
        # создание и размещение элементов, отвечающих за стоимость
        self.price_label = ttk.Label(text="Стоимость")
        self.price_entry = ttk.Entry()
        self.price_entry.grid(row=2, column=0, **p)
        self.price_label.grid(row=2, column=1, **p)
        # кнопка для продажи, указанного предмета
        # сюда прикрепить функцию для продажи
        self.sell_btn = ttk.Button(text="Продать")
        self.sell_btn.grid(row=3,
                           column=0,
                           columnspan=2
                           , **p)
        #подпись для отображения общего балланса
        self.total_label = ttk.Label(text="Ваш балланс: ")
        self.total_label.grid(row=4,
                              column=0,
                              columnspan=2,
                              **p)
        # создание списка предметов, которые есть в инвентаре

        self.inventory = tk.Variable(value=self.inv_items)
        self.items_list = tk.Listbox(
            height=13,
            width=40,
            listvariable=self.inventory
        )
        self.items_list.grid(row=0,
                             column=3,
                             rowspan=5,
                             **p)
        # создание меню
        menubar = Menu(self.win)
        self.win.config(menu=menubar)
        file_menu = Menu(menubar)
        # добавляем пункт в меню
        file_menu.add_command(
            label='Настройки',
            # вызываем метод settings_window, который открывает другое окно
            command=self.settings_window
        )
        # добавляем пункт в меню
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )


magaz = App()
#his paste expires in <1 hour. Public IP access. Share whatever you see with others in seconds with  Context. Terms of ServiceReport this