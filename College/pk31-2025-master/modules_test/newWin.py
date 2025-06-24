import tkinter as tk

class newWin():
    def __init__(self):
        self.nWin = tk.Tk()
        self.nWin.geometry("600x200")
        self.nWin.title("Второе окно")
        self.nWin.mainloop()
