from tkinter import *
from tkinter import ttk

class App: 
    def __init__(self): 
        self.win = Tk() #making a new class(сделали окошко)
        self.win.geometry("1280x720")#size
        self.win.title("Ещкере")#title and window size
        self.win.mainloop()#запуск
app = App()