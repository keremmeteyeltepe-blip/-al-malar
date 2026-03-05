import random
sifre = "1234567890!,*'^+%&/()=qwertyuıopğüasdfghjklşi,¨~.:-_QWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ"
uzunluk = int(input("parolanızın uzunluğu kaç ?"))

parola = ""
                                                                             
for i in range(uzunluk):
    parola += random.choice(sifre)
    print("...")

print("Parolanız:",parola)
