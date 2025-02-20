import tkinter as tk
from tkinter import ttk
class Item:
    def __init__(self):
        self.name = None
        self.price = None
class InventoryItem(Item):
    def __init__(self):
        self.quantity


class App: 
    def __init__(self): 
        self.win = tk.Tk() #making a new class(сделали окошко)
        self.win.geometry("1280x720")#size
        self.win.title("Ещкере")#title and window size
        self.setUI()
        self.win.mainloop()#запуск
        
    def setUI(self):
        p = {'padx':10,'pady':10}
        
        self.nameLbn = ttk.Label(text="Name")
        items = tk.StringVar()
        self.itemList = ttk.Combobox(textvariable=items)
        self.itemList.grid(row = 0, column=0,**p)
        self.nameLbn.grid(row=0,column=1,**p)
        
        self.quantityLbn=ttk.Label(text="Количество")
        self.quantityEntry = ttk.Entry()
        self.quantityEntry.grid(row=1,column=0,**p)
        self.quantityLbn.grid(row=1,column=1,**p)
        
        self.priceLbn = ttk.Label(text="Цена")
        self.priceEntry = ttk.Entry()
        self.priceLbn.grid(row=2,column=0,**p)
        self.priceEntry.grid(row=2,column=1,**p)
        
        self.sellbtn = ttk.Button(text="Sell")
        self.sellbtn.grid(row=3,column= 0,columnspan=2,**p)
        self.sellbtn = ttk.Button(text="купит")
        self.sellbtn.grid(row=2,column= 0,columnspan=1,**p)
        
        
        
        invItems = ["с","ос","ал"]
        self.inventory = tk.Variable(value = invItems)
        self.itemsListB = tk.Listbox(
            height=10,
            width=40,
            listvariable=self.inventory
        )
        self.itemsListB.grid(row=0,column=3,rowspan=5,**p)
        
        
initComponent = App()
