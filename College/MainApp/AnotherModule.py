import tkinter as tk 
class NewWin():
    def __init__(self):
        self.win= tk.Tk()
        self.win.geometry('600x300')
        self.win.title('secondary Window')
        
        self.win.mainloop()

    