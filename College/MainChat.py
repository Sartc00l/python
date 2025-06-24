from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget,QGridLayout,QListWidget,QLineEdit,QPushButton
from PyQt6.QtCore import QSize,Qt,QTimer
import pymysql.cursors
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connect()
        self.setWindowTitle("two 3.14doors")
        self.resize(QSize(1280,720))
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.message_view = QListWidget()
        self.message_entry = QLineEdit()
        
        send_message_btn = QPushButton("Sent")
        send_message_btn.clicked.connect(self.send_message)
        get_message_btn = QPushButton("Get")
        get_message_btn.clicked.connect(self.get_message)
        
        
        layout.addWidget(self.message_entry,0,0,1,1)
        layout.addWidget(self.message_view,2,0,1,2)
        layout.addWidget(get_message_btn,1,2)
        layout.addWidget(send_message_btn,1,1)
        self.get_message()
        self.show() 
        
    def send_message(self):
        try:
            self.cursor = self.cnx.cursor()
            with self.cursor:
                sql = "INSERT INTO messages(message) VALUES (%s)"
                prms=(self.message_entry.text(),)
                self.cursor.execute(sql,prms)
                self.cnx.commit()
            self.message_entry.clear()
            self.get_message()
        except pymysql.Error as e:
            raise Exception(f"не работает инсерт {e}")
    def get_message(self):
       try:
            self.cursor = self.cnx.cursor()
            sql="Select `message` FROM messages"
            with self.cursor:
                self.cursor.execute(sql)
                ans= self.cursor.fetchall()
              
            self.message_view.clear()
            for item in ans:
                self.message_view.addItem(item['message'])
            self.message_view.scrollToBottom()
       except pymysql.Error as e:
           raise Exception(f"НИМАГУ ПОЛУЧИТЬ СООБЩЕНИЯ {e}")
       
       QTimer.singleShot(2000,self.get_message)
       print("еще раз сработал")
       
       
    def db_connect(self):
        try:
            self.cnx = pymysql.connect(host="localhost",
                                        user='sqlPASSWORD123',
                                        password='123',
                                        database='dvaDolbaeba',
                                        charset='utf8mb4',
                                        port=8889,
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.cnx.cursor()
        except pymysql.Error as err: 
            raise Exception (f"ашибка {err}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()