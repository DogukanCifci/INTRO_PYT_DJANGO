import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable


my_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

R = requests.get(my_url)            #Burada url yi cektik

#print(R.text)           #Cektigimiz linkin bütün HTML Kodlarini almis olduk.

my_soup = BeautifulSoup(R.text, "html.parser") #Bu sekilde hata vermedi

#Burada film verilerini cekmek istedigimiz icin Chrome da gidip nerenin o filmlerin hepsini kapsadigini bulacagiz.
#tbody kismi bütün filmleri kapsiyor.

#my_list = my_soup.find_all("tbody") ---> yaparsam tbody olan hepsini almis olacak. Ama ben class üzerinden cekecigim icin all yazmiycam asagidaki gibi
my_list = my_soup.find("tbody", {"class":"lister-list"}).find_all("tr") 
#Burda yaptigim olay class= lister-list olan tbodylerin hepsini bul icinden tr leri veri olarak cek
#Ikinci find de find_all yaptim cünkü bütün tr leri almasini istiyorum. class ile cekmiyorum
film_list = list()
for filmler in my_list :
    names = filmler.find("td", {"class":"titleColumn"}).a.text      #Eger sadece . a yaparsak direk html kodundaki gibi tüm a yi verir.
    film_list.append(names)

    #Biz sadece ismini istedigimiz yani text kismini istedigimiz icin .a.text yaptik

my_list2 = my_soup.find("tbody", {"class":"lister-list"}).find_all("tr")
rating_list = list()
for i in my_list2 :
    rating = i.find("td", {"class":"ratingColumn imdbRating"}).strong.text
    rating_list.append(rating)

my_dict_films = zip(film_list, rating_list)     #Direk bir liste icinde film adi : rating formatta yazrdirmak icin
print(list(my_dict_films))

for k, v in zip(film_list, rating_list) :       #Film adi : rating  formatinda alt alta yazdirmak icin zip kullandim
    print(k, ':', v)



