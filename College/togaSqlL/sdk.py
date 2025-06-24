import toga
from toga.style.pack import ROW, COLUMN, Pack, RIGHT
import sqlite3


class App(toga.App):
    def button_handler(self, widget):
        
        tmp = self.login_entry.value
        tmp_password = self.pass_entry.value
        con = sqlite3.connect("parol.db")
        cur = con.cursor()
        cur.execute("SELECT parol FROM user WHERE login=?",(tmp,))
        ans = cur.fetchall()
        print(ans)
        if len(ans) > 0:
            p1 = ans[0]
            password = p1[0]
            if password == tmp_password:
                print("mojno")
                if self.notes_window == None:
                    self.notesWindow()
                else :
                    print("а тебе только одно окошечко")
            else:
                print("nemojno")
                

    def startup(self):
        self.notes_window = None
        
        self.main_window = toga.MainWindow()
        main_box = toga.Box()
        main_box.style.update(direction=COLUMN)
        login_box = toga.Box()
        login_box.style.update(direction=ROW)
        pass_box = toga.Box()
        pass_box.style.update(direction=ROW)

        button = toga.Button("Вход в систему", on_press=self.button_handler, style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        login_label = toga.Label("Логин", style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        pass_label = toga.Label("Пароль", style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        self.login_entry = toga.TextInput(style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        self.pass_entry = toga.PasswordInput(style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        login_box.add(login_label)
        login_box.add(self.login_entry)
        pass_box.add(pass_label)
        pass_box.add(self.pass_entry)
        main_box.add(login_box)
        main_box.add(pass_box)
        main_box.add(button)
        self.main_window.content = main_box
        self.main_window.show()

    def notesWindow(self):
        self.notes_window = toga.Window(title="Заметки")
        self.notes_box = toga.Box()
        self.notes_box.style.update(direction=COLUMN)
        self.note1 = toga.Button("Заметка1")
        self.note2 = toga.Button("Заметка2")
        self.note3 = toga.Button("Заметка3")
        self.note4 = toga.Button("Заметка4")
        self.note5 = toga.Button("Заметка5")
        self.notes_box.add(self.note1)
        self.notes_box.add(self.note2)
        self.notes_box.add(self.note3)
        self.notes_box.add(self.note4)
        self.notes_box.add(self.note5)
        self.notes_window.content = self.notes_box
        self.notes_window.show()
    def noteShow(self):
        self.note_window = toga.Window(title="Zametka")
        self.note_box=toga.Box()
        self.note_box.style.update(direction=COLUMN)
        
        
        


if __name__ == "__main__":
    app = App("Что-то на тоге", "оно есть")
    app.main_loop()


