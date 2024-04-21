from PyQt6.QtWidgets import *
import deneme

class loginEkrani(QMainWindow):
    def kontrol(self):
        kadi = self.ka.text()
        sifre = self.sf.text()
        #print("Tıklandı", kadi, sifre)
        if kadi == "admin" and sifre == "123":
            print("Giriş yapabilir.")
            deneme.pencere1()
        else:
            print("Hatalı kullanıcı adı veya şifre!")
        
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        icerik = QVBoxLayout() # layout oluşturduk Vertical
#icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre: "))
        self.sf = QLineEdit()
        icerik.addWidget(self.sf)
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
