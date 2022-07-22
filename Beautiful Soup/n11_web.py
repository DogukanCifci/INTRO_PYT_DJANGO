import requests 
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable

url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu"

R = requests.get(url)


soup = BeautifulSoup(R.text, "html.parser")

products = soup.find_all("li", {"class":"column"})

for product in products :
    isim = product.find("a", {"class" : "plink"}).h3.text
    fiyat = product.find("div", {"class" : "priceContainer"}).ins.text
    print(f'Ürün Isim : {isim} >> Ürün Fiyat {fiyat}')
    ürün_link = product.a.get("href")        #tag icindekini almak icin o tag ve .get methodu kullanilir .
    print(f'Ürün Linki : {ürün_link}')
    ürün_id = product.div.get("id")
    print(f'Ürün ID : {ürün_id}') 
   
#try-except icine alma sebebim siteye erisemezse kod icinde direk hata vermesin diye
    try :
        ürün_r = requests.get(ürün_link)        #For döngüsünde bunu yazarak her bir ürünün icine tiklamis gibi icerdeki bilgileri de cekicem.
        ürün_soup = BeautifulSoup(ürün_r.text,"html.parser")  #Yukarda ilk olusturdugumuz gibi. Iicne girdigimiz yeni linkin icinde artik arama yapabiliriz.
    except Exception as e :
        print(f'Siteye erisilemiyor. Hata Sebebi : {e}')

    özellik = ürün_soup.find("div", {"class" : "unf-prop-context"})
    özellikler = özellik.find_all("li")
    
    for bilgiler in özellikler :
        özellik_isim = bilgiler.find("p", {"class" : "unf-prop-list-title"}).text
        özellik_check = bilgiler.find("p", {"class" : "unf-prop-list-prop"}).text
        print(f'{özellik_isim} : {özellik_check}')
    print("-------------------------------------------------------------------------------------------------------")