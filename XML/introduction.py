import xml.etree.ElementTree as ET 

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    <date>09.02.1985</date>
    </person>'''

tree = ET.fromstring(data)          #Tirnak icindeki bütün veriler tek bir data ordan import ettigimiz kütüphane yardimiyla veriyi cekiyoruz.

print('Name : ', tree.find('name').text)            #Burda da veri icindeki istedigimiz veriyi özelligini belirterek aliyoruz.
print('Attr : ', tree.find('email').get('hide'))    #Burda icerdeki hide özeliginde ne yazdigini getirir.
print('Phone Type :', tree.find('phone').get('type'))   #Burdaki cikti da intl olacaktir. 
print('Number : ', tree.find('phone').text.lstrip())    #lstrip yapma sebebim numara asagida gözüküyordu.
print('Date : ', tree.find('date').text)

####Eger tag icindeki bir özelligi almak istiyorsak .text yerine .get('özellik_adi') ile ---- Tag arasindaki yaziyi almak istiyorsak .text ile aliyoruz.