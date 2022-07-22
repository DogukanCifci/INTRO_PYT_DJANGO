import requests
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_42.html"

R = requests.get(url)

Soup = BeautifulSoup(R.text, "html.parser")



degerler = Soup.find_all("tr")
my_list = list()
for i in degerler :
    deger = i.find("span", {"class":"comments"})
    my_list.append(deger)   
    
    print(deger)