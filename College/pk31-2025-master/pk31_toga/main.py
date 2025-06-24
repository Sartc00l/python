import toga
from toga.style.pack import ROW, COLUMN, Pack, RIGHT
import sqlite3


#https://github.com/leonid1123/pk31-2025/tree/master/pk31_toga
class App(toga.App):
    def button_handler(self, widget):
        tmp = self.login_entry.value
        tmp_password = self.pass_entry.value
        self.con = sqlite3.connect("passwords.db")
        self.cur = self.con.cursor()
        self.cur.execute("SELECT password FROM user WHERE login=?",(tmp,))
        ans = self.cur.fetchall()
        print(ans)
        if len(ans) > 0:
            p1 = ans[0]
            password = p1[0]
            if password == tmp_password:
                print("можно")
                self.notesWindow()
            else:
                print("неможно")

    def startup(self):
        self.user_id = 2
        self.style = Pack(padding=5, flex=1, font_family='Helvetica', font_size=16)
        self.notes_window = None
        self.main_window = toga.MainWindow()
        main_box = toga.Box()
        main_box.style.update(direction=COLUMN)
        login_box = toga.Box()
        login_box.style.update(direction=ROW)
        pass_box = toga.Box()
        pass_box.style.update(direction=ROW)

        button = toga.Button("Вход в систему", on_press=self.button_handler, style=self.style)
        login_label = toga.Label("Логин", style=self.style)
        pass_label = toga.Label("Пароль", style=self.style)
        self.login_entry = toga.TextInput(style=self.style)
        self.pass_entry = toga.PasswordInput(style=self.style)
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
        if self.notes_window is None:
            self.notes_window = toga.Window(title="Заметки")
            self.notes_box = toga.Box()
            self.notes_box.style.update(direction=COLUMN)
            self.note1 = toga.Button("Заметка1", on_press=self.noteShow,style=self.style)
            self.note2 = toga.Button("Заметка2",style=self.style)
            self.note3 = toga.Button("Заметка3",style=self.style)
            self.note4 = toga.Button("Заметка4",style=self.style)
            self.note5 = toga.Button("Заметка5",style=self.style)
            self.notes_box.add(self.note1)
            self.notes_box.add(self.note2)
            self.notes_box.add(self.note3)
            self.notes_box.add(self.note4)
            self.notes_box.add(self.note5)
            self.notes_window.content = self.notes_box
            self.notes_window.show()

    def noteShow(self, widget):
        self.note_window = toga.Window(title="Заметка")
        self.note_box = toga.Box()
        self.note_box.style.update(direction=COLUMN)
        self.note_view = toga.MultilineTextInput(style=self.style)
        self.note_win_btn = toga.Button("OK",style=self.style)
        self.note_box.add(self.note_view)
        self.note_box.add(self.note_win_btn)
        self.note_window.content = self.note_box
        self.cur.execute("SELECT note FROM notes WHERE id_user = 2")
        ans = self.cur.fetchone()
        print(ans)
        if ans:
            self.note_view.value = ans

        self.note_window.show()


if __name__ == "__main__":
    app = App("Что-то на тоге", "оно есть")
    app.main_loop()
