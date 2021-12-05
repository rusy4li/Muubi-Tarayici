import time
from selenium import webdriver


def sosyalmedya(sosg):
    browser = webdriver.Chrome(executable_path='driver/chromedriver')
    azap = webdriver.Chrome(executable_path='driver/chromedriver')
    noap = webdriver.Chrome(executable_path='driver/chromedriver')
    absup = webdriver.Chrome(executable_path='driver/chromedriver')
    browser.get("https://instagram.com/"+sosg)
    azap.get("https://facebook.com/"+sosg)
    noap.get("https://www.tiktok.com/@"+sosg)
    absup.get("https://tr.pinterest.com/"+sosg)
    time.sleep(1000)


print("Lütfen gireceğiniz 'ad-soyad' veya 'takma ad' değerlerini birleşik şekilde giriniz!")
print("Sosyal medya hesaplarını aramak istediğiniz kişinin 'ad-soyad' veya 'takma adı'?")
sos = str(input("->> "))
print(sosyalmedya(sos))
time.sleep(10)
