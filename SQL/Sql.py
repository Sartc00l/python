import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import mysql.connector.locales.eng.client_error


class TableDb:
    def __init__(self,_id,_size,_color,_price):
        self.size = _size
        self.color = _color
        self.price = _price
        self.id =_id
    def __str__(self):
        return f"id {self.id} name {self.color} price {self.price} size {self.size}"

class MySQLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DB")
        #настройка подключения
        self.db_config = {
            'host': 'localhost',
            'user': 'sqlPASSWORD123',  
            'password': '123',  
            'database': 'shopObuv',
            'port':'8889'
        }
        
        self.connection = None
        self.connect_to_db()
        
        
        self.create_widgets()
        self.show_records()
        
    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                print("Mojno rabotat")
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться к MySQL: {e}")
    

    def create_widgets(self):
        # Поля ввода
        tk.Label(self.root, text="Size  :").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.size_entry = tk.Entry(self.root)
        self.size_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.root, text="Color:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.root, text="Price:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.color_entry = tk.Entry(self.root)
        self.color_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Кнопки
        self.add_button = tk.Button(self.root, text="Добавить запись", command=self.add_record)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.del_button = tk.Button(self.root, text="удалить ", command=self.del_kbd)
        self.del_button.grid(row=5, column=1, padx=5, pady=5)
        
        self.show_button = tk.Button(self.root, text="Показать записи", command=self.show_records)
        self.show_button.grid(row=3, column=1, padx=5, pady=5)
        
        # Listbox для отображения записей
        self.records_listbox = tk.Listbox(self.root, width=50, height=10)
        self.records_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # Полоса прокрутки
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.config(command=self.records_listbox.yview)
        self.scrollbar.grid(row=4, column=2, sticky="ns")
        self.records_listbox.config(yscrollcommand=self.scrollbar.set)
    
    def add_record(self):
        size = self.size_entry.get()
        price = self.price_entry.get()
        color = self.color_entry.get()

        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO obuv (size, color, price) VALUES (%s, %s, %s)"#тут свою табличку введите
            cursor.execute(query, (size, price, color))
            self.connection.commit()
            messagebox.showinfo("Успех", "Запись успешно добавлена")
            self.clear_entries()
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить запись: {e}")
    
    def show_records(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM obuv")#obuv на свое имя таблицы 
            records = cursor.fetchall()
            
            self.records_listbox.delete(0, tk.END)
            
            
            for record in records:
                record_str = f"ID: {record[0]}, Имя: {record[1]}, Возраст: {record[2]}, Email: {record[3]}"
                self.obuv = TableDb(record[0],record[1],record[2],record[3])
                self.records_listbox.insert(tk.END, self.obuv)
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось получить записи: {e}")
        print(self.obuv)
        
    
    
    def del_kbd(self):
        cursor = self.connection.cursor()
        #del_str ="DELETE FROM 'Gdeto' WHERE 'tipa id' ={'nasha hren'} "
        self.num = self.records_listbox.curselection()
        if self.num:
            self.num = self.num[0]
        print(f"ВЫБРАЛ ВОТ ЕТО {self.num}")
        #cursor.execute(del_str,(self.num,))
       #self.connection.commit()
        self.show_records()
    
    def clear_entries(self):
        self.size_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
    
    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Соединение с MySQL закрыто")

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = MySQLApp(root)
    root.mainloop()