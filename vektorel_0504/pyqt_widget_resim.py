from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilebilecek değer:"))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç:"))
        # icerik.addWidget(QPixmap('login.png')) 

        xx = QPixmap('login.png.png')
        lab = QLabel()
        lab.setPixmap(xx)
        icerik.addWidget(lab)

        pencereicerigi = QWidget()
        pencereicerigi.setLayout(icerik)
        self.setCentralWidget(pencereicerigi)

app = QApplication([])        

pencere = girisPenceresi()
pencere.show()

app.exec()
