import random


class TasKagitMakasOyunu():

    def __init__(self):
        self.secim()
    def secim(self):
        giris="TAŞ KAĞIT MAKAS OYUNUNA HOŞGELDİNİZ."
        print("&"* len(giris),giris,"&" * len(giris), sep="\n",end="\n")
        while True:
            secme=input("Oyun Hakkında Bilgi Almak isterseniz 1 e Oyuna Başlamak İsterseniz 0 a Tıklayınız.")

            if secme == "1":
                self.oyunHakkindaBilgi()
            elif secme=="0":
                self.tasKagitMakasOyunu()
            else:
                print("Geçersiz bir ifade girdiniz işleminiz iptal ediliyor...")
                break

    def oyunHakkindaBilgi(self):
        print("""OYUN HAKKINDA BİLGİ --->
        Taş Kağıt Makas Oyunu:
        Önce kullanıcı bir seçim yapıyor.Kullanıcıya karşılık olarak bilgisayarda bir seçim yapıyor.
        İki oyuncunun 3 durumdan birinin seçimesiyle oynanıyor("Taş" veya "Makas" veya "Kağıt"
        Kazanma durumları:
        Taş, makası kırarak yener.
        Kağıt, taşı sararak yener.
        Makas, kağıdı keserek yener.
        Oyun bu verilerden baska veri girilene kadar devam eder. 
        """)

    def tasKagitMakasOyunu(self):
        secimler=["TAŞ","MAKAS","KAĞIT","1","2","3"]

        while True:
            kullanici=input("1){}\n2){}\n3){}\nseçiniz--->".format(*secimler)).upper()
            bilgisayar=random.randrange(0,3)
            sayi=-1

            if kullanici in secimler:
                if kullanici=="1" or kullanici=="TAŞ":
                    sayi=0

                elif kullanici=="2" or kullanici=="KAĞIT":
                    sayi=1

                elif kullanici=="3" or kullanici=="MAKAS":
                    sayi=2


                if sayi==bilgisayar:
                    print("Berabare, sen {} yaptın ----> Ben de {} yaptım".format(secimler[sayi],secimler[bilgisayar]))
                elif sayi==0 and bilgisayar==1:
                    print("Ben kazandım,sen {} yaptın----> Ben {} yaptım.".format(secimler[sayi],secimler[bilgisayar]))
                elif sayi==0  and bilgisayar==2:
                    print("Sen kazandın,sen {} yaptın----->Ben {} yaptım.".format(secimler[sayi],secimler[bilgisayar]))
                elif sayi==1 and bilgisayar==2:
                    print("Ben kazandım, sen {} yaptın------> Ben {} yaptım.".format(secimler[sayi],secimler[bilgisayar]))
                elif sayi==1 and bilgisayar==0:
                    print("Sen kazandın, sen {} yaptın------> Ben {} yaptım.".format(secimler[sayi],secimler[bilgisayar]))
                elif sayi==2 and bilgisayar==0:
                    print("Ben kazandım, sen {} yaptın------> Ben {} yaptım.".format(secimler[sayi],secimler[bilgisayar]))
                elif sayi==2 and bilgisayar==1:
                    print("Sen kazandın, sen {} yaptın------>Ben {} yaptım.".format(secimler[sayi],secimler[bilgisayar]))

                print()
            else:
                print("Oyun Sona Erdi. Başa Döndünüz!!!")
                break


if __name__=="__main__":
    TasKagitMakasOyunu()

        


