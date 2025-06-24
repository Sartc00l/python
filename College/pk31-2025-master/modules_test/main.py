import tkinter as tk
import newWin as nW


class App:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("600x300")
        self.win.title("Первое окно")
        self.btn = tk.Button(text="Click", command=nW.newWin)
        self.btn.pack()
        self.win.mainloop()





if __name__ == "__main__":
    app = App()
