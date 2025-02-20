from tkinter import *

def calc(): 
    tmp = mark_entry.get()
    tmp_mark = int(tmp)
    marks.append (tmp_mark)
    sr_mark =sum(marks)/len(marks)
    result_Label ["text"] = f"Средний балд: {sr_mark}"
    

marks = []

win = Tk()
win.geometry("200x200")
win.title("Средний балл")

Fname_Label = Label(text="Фамилия")
Group_Label = Label (text="Группа")
result_Label = Label (text="Средний балл")

Fname_entry = Entry() 
Group_entry = Entry()
mark_entry = Entry()

btn = Button(text="Добавить",command=calc)

Fname_Label.grid(row=0, column=0, padx=5, pady=5)
Fname_entry.grid(row=0,column=1, padx=5, pady=5)
Group_Label.grid(row=1, column=0,padx=5,pady=5)
Group_entry.grid(row=1, column=1,padx=5, pady=5)
btn.grid(row=2, column=0, padx=5, pady=5) 
mark_entry.grid(row=2, column=1, padx=5, pady=5)
result_Label.grid(row=3, column=0, columnspan=2, padx=5, pady=5) 
win.mainloop()
