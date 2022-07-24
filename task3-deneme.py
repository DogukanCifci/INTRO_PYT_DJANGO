import requests
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_1462205.html"

R = requests.get(url)

Soup = BeautifulSoup(R.text, "html.parser")



degerler = Soup.find_all("tr")
toplam = 0
for item in degerler :
    try :
        count = item.find('span', {'class' : 'comments'}).text
        count = int(count)
        toplam += count
    except Exception as e :
        print('Hata ver : {}'.format(e))

print(f'Toplam : {toplam}')