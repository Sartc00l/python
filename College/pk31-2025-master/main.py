import sys

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QDateEdit, QPushButton, QListWidget, \
    QMessageBox
from qt_material import apply_stylesheet
import pymysql.cursors


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_list = []
        self.setWindowTitle('Hello World')
        layout = QGridLayout()
        name_label = QLabel("ИМЯ")
        self.name_entry = QLineEdit()
        fam_label = QLabel("ФАМИЛИЯ")
        self.fam_entry = QLineEdit()
        group_label = QLabel("ГРУППА")
        self.group_entry = QLineEdit()
        kurs_label = QLabel("КУРС")
        self.kurs_entry = QLineEdit()
        date_of_birth_label = QLabel("ДАТА РОЖДЕНИЯ")
        self.date_of_birth_entry = QDateEdit()
        phone_label = QLabel("ТЕЛЕФОН")
        self.phone_entry = QLineEdit()
        self.add_btn = QPushButton("ДОБАВИТЬ")
        self.add_btn.clicked.connect(self.get_values)
        self.student_view = QListWidget()
        self.student_view.itemSelectionChanged.connect(self.student_selected)
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.name_entry, 0, 1)
        layout.addWidget(fam_label, 0, 2)
        layout.addWidget(self.fam_entry, 0, 3)
        layout.addWidget(group_label, 1, 0)
        layout.addWidget(self.group_entry, 1, 1)
        layout.addWidget(kurs_label, 1, 2)
        layout.addWidget(self.kurs_entry, 1, 3)
        layout.addWidget(date_of_birth_label, 2, 0)
        layout.addWidget(self.date_of_birth_entry, 2, 1)
        layout.addWidget(phone_label, 2, 2)
        layout.addWidget(self.phone_entry, 2, 3)
        layout.addWidget(self.add_btn, 3, 0, 1, 4)
        layout.addWidget(self.student_view, 4, 0, 1, 4)
        self.setLayout(layout)
        apply_stylesheet(app, theme='light_red.xml')
        self.db_connect()
        self.get_all_students()
        self.show()

    def get_values(self):
        sql = """INSERT INTO 
                students(name,fam_name,stud_group,kurs,date_of_birth,phone)
                VALUES (%s,%s,%s,%s,%s,%s)"""
        name = self.name_entry.text()
        fam = self.fam_entry.text()
        group = self.group_entry.text()
        kurs = self.kurs_entry.text()
        dr = self.date_of_birth_entry.text()
        phone = self.phone_entry.text()
        if name and fam and group and kurs and dr and phone:
            params = (name, fam, group, kurs, dr, phone)
            self.cur.execute(sql, params)
            self.cnx.commit()
            self.get_all_students()
            #self.student_view.addItem(f"{name},{fam},{group},{kurs},{dr},{phone}")
        else:
            QMessageBox.critical(
                self,
                'Внимание ',
                'Криворукость детектед! \nНУЖНО ВСё заполнить!!!'
            )

    def db_connect(self):
        self.cnx = pymysql.connect(
            host="localhost",
            user="pk31",
            password="1234",
            database="students"
        )
        self.cur = self.cnx.cursor()

    def get_all_students(self):
        sql = "SELECT * FROM students"
        self.cur.execute(sql)
        ans = self.cur.fetchall()
        self.student_view.clear()
        self.id_list = []
        for item in ans:
            tmp = f"{item[1]},{item[2]},{item[3]},{item[4]},{item[5]},{item[6]}"
            self.student_view.addItem(tmp)
            self.id_list.append(item[0])

    def student_selected(self):
        tmp = self.student_view.currentRow()
        selected_id = self.id_list[tmp]
        print(selected_id)
        self.add_btn.setText("Изменить")
        sql = "SELECT * FROM students WHERE id=%s"
        params=(selected_id,)
        self.cur.execute(sql, params)
        ans = self.cur.fetchall()
        tmp = ans[0]
        self.name_entry.setText(tmp[1])
        self.fam_entry.setText(tmp[2])
        self.group_entry.setText(tmp[3])
        self.kurs_entry.setText(str(tmp[4]))

        brrr=str(tmp[5])
        year, month, day = map(int, brrr.split('-'))
        qdate = QDate(year, month, day)
        self.date_of_birth_entry.setDate(qdate)

        self.phone_entry.setText(tmp[6])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
