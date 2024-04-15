from PyQt6.QtWidgets import *

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilebilecek değer:"))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç:"))
        
        pencereicerigi = QWidget()
        pencereicerigi.setLayout(icerik)
        self.setCentralWidget(pencereicerigi)

app = QApplication([])        

pencere = girisPenceresi()
pencere.show()

app.exec()
