import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel


class AdditionalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Новое окно")
        self.setGeometry(200, 200, 300, 200)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Это новое окно"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Открытие окна")
        self.setGeometry(100, 100, 400, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        button = QPushButton("Открыть окно")
        button.clicked.connect(self.open_window)
        layout.addWidget(button)
        
        central_widget.setLayout(layout)
    
    def open_window(self):
        self.new_window = AdditionalWindow()
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())