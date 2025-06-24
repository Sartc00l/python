from PyQt6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QLabel,QDialog,QDialogButtonBox,QVBoxLayout
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtGui import QPixmap

import sys 
class CustomDiag(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("ВНИМАНИЕ")
        QBtn=(
            QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        layout = QVBoxLayout()
        message = QLabel("Сосал?)")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fapp")
        self.setMaximumSize(QSize(1440,900))
        self.setMinimumSize(QSize(720,720))
        btn  = QPushButton("НАЖМИ КНОПОЧКУ ПЖПЖЖПП")
        btn.setStyleSheet("font-size: 32px;")
        btn.setCheckable(True)
        btn.clicked.connect(self.btn_pressed)
        self.setCentralWidget(btn)
    def btn_pressed(self):
            qdiag = CustomDiag()
            layout = QVBoxLayout()
            widget = QWidget()
            if qdiag.exec():
                txt_lbn = QLabel("СОСУНИШКА\nАХХАХАХАХА") 
                txt_lbn.setStyleSheet("font-size: 32px;")
                layout.addWidget(txt_lbn)
                lbn = QLabel(self)
                image = QPixmap('joker.jpeg')
                lbn.setPixmap(image)    
                lbn.setScaledContents(True)
                self.resize(image.width(),image.height())
                lbn.setAlignment(Qt.AlignmentFlag.AlignCenter)
                txt_lbn.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(lbn)
                widget.setLayout(layout)
                
                self.setCentralWidget(widget)
            else:
                self.btn_pressed()
                
            
app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec()