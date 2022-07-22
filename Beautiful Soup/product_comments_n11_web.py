import requests 
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable

url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu"

R = requests.get(url)

Soup = BeautifulSoup(R.text, "html.parser")

product_list = Soup.find_all("li", {"class" : "column"})

for product in product_list :
    comment_number = 0
    product_link = product.a.get("href")
    print(product_link)
    

    try :
        new_R = requests.get(product_link)
        new_Soup = BeautifulSoup(new_R.text, 'html.parser')
    except Exception as e :
        print(f'Siteye Ulasilamiyor. Hata Mesaji : {e}')

    comments_list = new_Soup.find_all("li", {"class":"comment"})
    for comment in comments_list :
        comment_number += 1
        try :
            comment_title = comment.find("h5", {"class":"commentTitle"}).text
            print(f'{comment_number}. {comment_title}')
        except :
            print(f'{comment_number}.')
            

        product_comment = comment.find("p").text
        print(f'***{product_comment}')
        print()
    print('----'*20)