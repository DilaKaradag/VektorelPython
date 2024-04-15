from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget 

class girisPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevirilecek değer:"))
        icerik.addWidget(QLineEdit())
        hesapla = QPushButton("Çevir")
        icerik.addWidget(hesapla)
        hesapla.clicked.connect(self.mesajGoster)
        icerik.addWidget(QLabel("Sonuç:"))

        pencereIcerigi = QWidget()
        pencereIcerigi.setLayout(icerik)
        self.setCentralWidget(pencereIcerigi)

    def hesaplama(self):
        print("Butona tıklandı.")

    def mesajGoster(self):
        mesaj = QMessageBox()
        mesaj.setText("Butona tıklandı")
        mesaj.exec()

app = QApplication([])

pencere = girisPenceresi()
pencere.show()

app.exec()
