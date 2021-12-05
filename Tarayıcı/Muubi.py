# -*- coding:utf-8 -*-
# Hoşgeldiniz Bu Program rusy4 Adlı GitHub Kullanıcısı Tarafından Kodlanmıştır!
# Muubi +Gelişmiş Tarayıcı
import time
from selenium import webdriver
import os


def help(f):
    if f == "1":
        return "Muubi mini ama Güvenilir ve Doğru bilgi veren bir tarayıcıdır."
    elif f == "2":
        return "Muubi'yi açtıktan sonra istediğiniz zaman vikipedi diyerek vikipedi ile arama özelliğini etkinleştirebilirsiniz."
    elif f == "3":
        return "Muubi'yi açtıktan sonra 'ara' veya 'Ara' yazarak güvenilir şekilde arama yapabilirsiniz."
    elif f == "4":
        return "Muubi'yi açtıktan sonra 'sosyalmedya' veya 'sosyal medya' yazarak istediğiniz kişinin sosyal medya hesaplarını bulma özelliğini etkinleştirebilirsiniz."
    elif f == "5":
        return "Selam ben Burak, yani rusy4li. 1 yıla yakındır yazılımla uğraşıyorum.\nİlk öğrenmeye başladığım dil 'C#', C#'ın temelini kavradıktan sonra sıkıldığımı farkedip bir süre ara verdim,\ndaha sonra ise Front-End Geliştirici olarak yazılıma devam ettim fakat çevremdeki herkesin sağlam projeler yaparken benim boş site tasarımlarıyla uğraşmam çok sıkıcı geliyordu.\n Bende bu yüzden python ile yoluma devam etmeye karar verdim. "


print("""
.___  ___.  __    __   __    __  .______    __  
|   \/   | |  |  |  | |  |  |  | |   _  \  |  | 
|  \  /  | |  |  |  | |  |  |  | |  |_)  | |  | 
|  |\/|  | |  |  |  | |  |  |  | |   _  <  |  | 
|  |  |  | |  `--'  | |  `--'  | |  |_)  | |  | 
|__|  |__|  \______/   \______/  |______/  |__| 
                                                
""")
print("Muubi'de arama yapın")
print("'help' yazarak yardım alabilirsiniz!")
while True:
    sorgu = input("->> ")

    if (sorgu.lower() == "sosyalmedya") or (sorgu.lower() == "sosyal medya"):
        os.chdir("functions")
        os.startfile("sosyalmedya.py")

    if sorgu.lower() == "vikipedi":
        print("Vikipedi de aramak istediğiniz içerik veya bilgi nedir?")
        search = input("->> ")
        browser = webdriver.Chrome(executable_path='C:/driver/chromedriver')
        browser.get("https://tr.wikipedia.org/wiki/")
        time.sleep(2)
        txtsearch = browser.find_element_by_name('search')
        txtsearch.send_keys(search)
        time.sleep(3)

    if sorgu.lower() == "ara":
        print("")
        print("Muubi Tarayıcısı ile aramak istediğiniz şey nedir?")
        search = input("->> ")
        print(".")
        print(".")
        print("Güvenilir bir şekilde Doğru bilgi aranıyor")
        time.sleep(0.5)
        print(".")
        browser = webdriver.Chrome(executable_path='driver/chromedriver')
        browser.get("https://startpage.com/?sc=UF5nNQMROb6j20&t=dark")
        time.sleep(2)
        txtsearch = browser.find_element_by_id('q')
        txtsearch.send_keys(search)
        time.sleep(1)
        login_btn = browser.find_element_by_class_name("ico")
        login_btn.click()

    if sorgu.lower() == "help":
        print("<(1)> Muubi Hakkında bilgi almak istiyorum")
        print("<(2)> vikipedi ile nasıl arama yaparım?")
        print("<(3)> Muubi ile nasıl güvenilir ve doğru arama yaparım?")
        print("<(4)> Sosyal medya hesap bulma özelliğini nasıl kullanırım?")
        print("<(5)> Muubi'yi yapan kişi Hakkında bilgi almak istiyorum")
        print("Öğrenmek istediğiniz bilginin numarasını girin lütfen")
        g = input("->> ")
        print(help(g))
    else:
        print("'Ara' komutunu vererek Muubi'nin sizi güvenilir arama adresine bağlamasını sağlayın.")
