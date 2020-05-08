# -*- coding: utf-8 -*-

# @raifpy | t.me/BetikSonu 

from __future__ import print_function # Python 2.7 kullananlarda print fonksiyonunun hata vermemesi için
import os
import sys
import time
#import shutil
#import base64
import requests 
import random 
import threading
from bs4 import BeautifulSoup





class printscreen():
    def __init__(self,gorsel_tanim=False,sleep=2):
        self.gorsel = gorsel_tanim
        self.header={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        
        self.url = "https://prnt.sc/"
        
        self.boolean = [True,False,None] # 3 modülde olacak random elemanlarımız : harf+sayi | harf | sayi
        
        self.harf_kumelenmesi = "q w e r t y u i o p a s d f g h j k l z x c v b n m".split() # Türkçe Q kalvyemden sıra ile bassarak yaptım :D Eksik olabilir
        
        if gorsel_tanim:
            self.gorseltanıma()
        
        while 1:
            threading.Thread(target=self.betikle).start()
            time.sleep(sleep) # 2 saniye bekleyip yeni işlemi

    
    def gorseltanıma(self):
        try:
            import pytesseract
            from PIL import Image
            from io import BytesIO
            image = Image.open("rm.png")
            self.text = pytesseract.image_to_string(image)

            self.BytesIO = BytesIO
            self.Image = Image
            self.pytesseract = pytesseract

        except ModuleNotFoundError as hata:
            print(hata)
            input("Modül dahil edilemedi . Görsel tanımlama es geçiliyor !")

        except FileNotFoundError:
            input("Örnek resim bulunamadı . Görsel tanımlama es geçiliyor !")

        except Exception as hata:
            print("HATA :\n\n")
            print(hata)
            print("\n\nÇözüm : https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i")
            input("\nGörsel tanımlama es geçiliyor .")

        else:
            self.gorsel = True
            print("Görsel tanımlama aktif !")
            print("404 metni : \n\n{}".format(self.text)+"\n\n")

    
    def betikle(self):
        if not os.path.exists("imgs"):
            os.mkdir("imgs")


        sonuc = random.choice(self.boolean)
        if sonuc:
            kelam = ""
            for i in range(random.randint(3,5)):
                kelam += random.choice(self.harf_kumelenmesi)
            kelam += str(random.randint(1,9999))
            rndm = kelam
        
        elif sonuc == False:
            kelam = ""
            for i in range(random.randint(3,6)):
                kelam += random.choice(self.harf_kumelenmesi)

            rndm = kelam
        
        elif sonuc == None:
            rndm = str(random.randint(1,99999))
        
        else:
            return

        self.istek(rndm)

    def istek(self,rndm):
        try:
            print(self.url+rndm)
            abc = requests.get(self.url+rndm,headers=self.header)
            if not abc.status_code == 200:
                print("200 dönmeyen kod ! {}".format(abc.status_code))
                return
            
            
            kaynak = BeautifulSoup(abc.text,"lxml")
            image = kaynak.find("img")
            if image:
                image = image["src"]
                
                if image.startswith("//"):
                    image = image.lstrip("//")

                if not image.startswith("http"):
                    image = "http://"+image

                if image == "https://st.prntscr.com/2020/05/08/0312/img/0_173a7b_211be8ff.png" or image == "http://st.prntscr.com/2020/05/08/0312/img/0_173a7b_211be8ff.png":
                    print("404 | \033[31mDefault 404\033[0m image | {}".format(rndm))
                    return

                source = requests.get(image).content # resmin rb hali .
                self.isle(source,rndm)

        except KeyboardInterrupt:
            sys.exit()

    def isle(self,source,rndm):
        if not self.gorsel:
            with open("imgs/{}.png".format(rndm),"wb") as png:
                png.write(source)
                print("\033[32m{}.png yazıldı !\033[0m | gorsel = False".format(rndm))


        else:
            text=""
            print("\033[33m{} işleniyor !\033[0m".format(rndm))
            
            try:
            
                image = self.BytesIO(source) # rb kaynak kodunu PIL'ın okuyabileciği formata çevirdik
                img = self.Image.open(image) # PIL ile resmi açtık
                text=self.pytesseract.image_to_string(img) # pyte.. ile resmi yazıya çevirdik 
            
            except:
                print("Işlenemedi !")
            
            print("----------------------")
            
            if text == self.text:
                print("\033[31m404\033[0m image ile aynı veri | {} ..".format(rndm))
                
            else:
                with open("imgs/{}.png".format(rndm),"wb") as png:
                    png.write(source)

                print("\033[32m{}.png yazıldı !\033[0m | \033[31m{}\033[0m".format(rndm,text))





        
        








if __name__ == "__main__":
    printscreen()
    #printscreen(gorsel_tanim=True)