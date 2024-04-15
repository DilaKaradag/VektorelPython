from PyQt6.QtWidgets import *

class loginEkrani(QMainWindow):
    def kontrol(self):
        print("Tıklandı")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        icerik = QVBoxLayout() # layout oluşturduk Vertical
#icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))
        ka = QLineEdit()
        icerik.addWidget(ka)
        icerik.addWidget(QLabel("Şifre: "))
        sf = QLineEdit()
        icerik.addWidget(sf)
        buton1 = QPushButton("Çevir")
        icerik.addWidget(buton1)
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        buton1.clicked.connect(self.kontrol)

uygulama = QApplication([])
pencere = loginEkrani()
pencere.show()
uygulama.exec()
