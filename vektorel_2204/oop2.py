class Ogrenci:
    TC = "000000000"
    ad = "Tanımsız"
    no = 000
    def __init__(self,xx,yy):
        print("Ogrenci sınıfının init fonksiyonu çalıştı")
        self.ad = xx
        self.no = yy
    def bilgiVer(self):
        print("Metod ile bilgi veriliyor: Adı:" ,self.ad,"Numarası:",self.no)

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741)

#print(ogrenci1.ad)
#print(ogrenci1.no)
ogrenci1.bilgiVer()