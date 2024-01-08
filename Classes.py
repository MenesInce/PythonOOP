# class <Class Name>():
#     <class attr>    ### class attrbute, genel değerleri içerir
# def __init__(self,<attr>): ### init,instantiation yani örneklendirmenin kısaltmasıdır.
#     self.<instance attr> = attr ### instance attribute'lar, oluşturulan örneğe özgüdür
#     ...

# def <method>(self,<params>): ### methodlar class'a özgü fonksiyonlardır
#     ...
#     return ...



#* Class Oluşturma

class Ucus():
    havaYolu = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu) :
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    # dunder methodlar 
    def __repr__(self) : #(yeni bir obje oluşturulduğunda ekrana basılacak olan mesaj)
        return "{} sefer sayili {} -- {} uçuş, sistemde oluşturulmuştur.".format(self.kod,self.kalkis,self.varis)

    def anons_yap(self) :
        return "{} sefer sayili {} -- {} uçuşumuz {} dakika sürecektir".format(self.kod,self.kalkis,self.varis,self.sure)
       
    
    def koltuk_sayisi_guncelle(self) :
        return "Boş koltuk sayisi : {} ".format(self.kapasite - self.yolcu)
  
    
    def bilet_satis(self, bilet_adedi = 1) :
        if self.yolcu + bilet_adedi <= self.kapasite : 
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print("{} adet bilet satılmıştır. {}".
                format(bilet_adedi,self.koltuk_sayisi_guncelle()))
        else :
            print("{} adet bilet, mevcut bilet sayısını aşmaktadır. Yetersiz koltuk sayısı".format(bilet_adedi))




ucus1 = Ucus("TK123","IST","ANK",60,300,50)
print(ucus1.kod)

print("--------------------------------------------")

ucus2 = Ucus("TK125","BOD","ANT",40,200,98)
print("Ucus 2 yolcu kapasitesi : {} kişi. Mevcut yolcu sayisi : {} kişi".format(ucus2.kapasite,ucus2.yolcu))
print(ucus2.anons_yap())
print(ucus2.koltuk_sayisi_guncelle())
ucus2.bilet_satis(5)

print("--------------------------------------------")

ucus3 = Ucus("TK125","ELZ","ANT",120,250,200)
print("Ucus 3 yolcu kapasitesi : {} kişi. Mevcut yolcu sayisi : {} kişi".format(ucus3.kapasite,ucus3.yolcu))
print(ucus3.anons_yap())
print(ucus3.koltuk_sayisi_guncelle())
ucus3.bilet_satis(49)
print(ucus3.koltuk_sayisi_guncelle())

print("--------------------------------------------")

print(ucus3)


















