# class Seyehat():
#     def __init__(self,kalkis,varis) :
#         self.kalkis = kalkis
#         self.varis = varis

#     def anons(self) :
#         return "{} - {} seyahatine HOŞ GELDİNİZ!".format(self.kalkis, self.varis)
    

# class Otobus(Seyehat) : 
#     def __init__(self,mola_duraklari) :
#         Seyehat.__init__(self,"IST","ANK")
#         self.mola_duraklari = mola_duraklari


# seyehat1 = Seyehat("ANT","BOD")
# print(seyehat1.anons())
# print(seyehat1.kalkis , seyehat1.varis)

# print("-----------------------------")
# oto1 = Otobus(["FET","ALAN"])
# print(oto1.mola_duraklari)
# print(oto1.kalkis)
# print(oto1.anons())
        

class Seyehat():
    def __init__(self,kalkis,varis) :
        self.kalkis = kalkis
        self.varis = varis

    def anons(self) :
        return "{} - {} seyahatine HOŞ GELDİNİZ!".format(self.kalkis, self.varis)
    

class Otobus(Seyehat) : 
    def __init__(self,mola_duraklari, kalkis, varis) :
        
        Seyehat.__init__(self,kalkis,varis)
        self.mola_duraklari = mola_duraklari


seyehat1 = Seyehat("ANT","BOD")
print(seyehat1.anons())
print(seyehat1.kalkis , seyehat1.varis)

print("-----------------------------")
oto1 = Otobus(["FET","ALAN"],"ANT","ANK")
print(oto1.mola_duraklari)
print(oto1.anons())
print("Kalkış : " , oto1.kalkis)
print("Varış : " , oto1.varis)

        