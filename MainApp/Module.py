import tkinter as tk 
import AnotherModule
class SettingsWind:
    def __init__(self):
        self.win= tk.Tk()
        self.win.geometry('600x300')
        self.win.title('Window')
        self.btn = tk.Button(text='Click',command=AnotherModule.NewWin)
        self.btn.grid(row=0,column=1)
        self.btn.pack()
        self.win.mainloop()
        

loadApp = SettingsWind()
    