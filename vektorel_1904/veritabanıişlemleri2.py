import sqlite3

xxx = sqlite3.connect("rehber2.db")

secilenvt = xxx.cursor()

ad = input("Ad soyad:")
tel = input("Telefon:")

secilenvt.execute("INSERT INTO ogrenciler (adSoyad, tc) VALUES('{ad}','{tc}')")
xxx.commit()

