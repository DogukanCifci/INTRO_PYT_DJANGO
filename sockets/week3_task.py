import requests
from bs4 import BeautifulSoup

my_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

R = requests.get(my_url)            #Burada url yi cektik

print(R.text)           #Cektigimiz linkin bütün HTML Kodlarini almis olduk.