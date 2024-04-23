import sqlite3

xxx = sqlite3.connect("okul2.db")

secilen = xxx.cursor()

secilen.execute("CREATE TABLE IF NOT EXISTS ogrenciler(adSoyad, tc)")
secilen.execute("INSERT INTO ogrenciler(adSoyad, tc) VALUES ('Sena','42341234')")
xxx.commit()                

