import requests 
from bs4 import BeautifulSoup
url = input("Web sayfasini giriniz : ")

R = requests.get(url)

my_soup = BeautifulSoup(R.text,"html.parser")

my_list = my_soup.find("tbody", {"class" : "lister-list"})

my_list2 = my_list.find_all("tr")

for i in my_list2 :
    names = i.find("td", {"class":"titleColumn"}).a.text
    tarih = i.find("td", {"class":"titleColumn"})
    tarihler = tarih.find("span", {"class":"secondaryInfo"}).text.strip("()")       #sagdan soldan parantezi kaldirdik
    

    print(f'Film Ismi : {names} >> Film Yayin Tarih : {tarihler} ')

       