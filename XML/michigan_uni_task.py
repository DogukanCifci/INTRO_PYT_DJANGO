import xml.etree.ElementTree as ET
import urllib.request as ur

#Dosya acma islemi
my_url = input('Enter the url : ')                          #http://py4e-data.dr-chuck.net/comments_42.xml
print(my_url, 'is retrieving')                              #http://py4e-data.dr-chuck.net/comments_1462207.xml
xml = ur.urlopen(my_url).read()


#dosyadaki veriler alindiktan sonra icerdeki veriyi cekme isleme
tree = ET.fromstring(xml)
print(len(xml), 'retrieved')            #Total number of characters
lst = tree.findall('comments/comment')
print('Sayi :', len(lst))
total = 0
for item in lst :
    numb = item.find('count').text
    try :
        numb = int(numb)
        total += numb
    except Exception as e:
        print('That is not a number! The Problem : {}'.format(e))

print('Total = ', total)