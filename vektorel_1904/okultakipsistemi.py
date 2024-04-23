import sqlite3
veriTabanı = sqlite3.connect('okultakipsistemi.db') # varsa bağlan, yoksa oluştur.
secilenvt = veriTabanı.cursor()

def tabloOlustur():
    secilenvt.execute("CREATE TABLE ogrenciler(adSoyad, numara) ")
    veriTabanı.commit()
    veriTabanı.close()

tabloOlustur()