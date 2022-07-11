import re 
x = "My 2 favorite numbers are 19 and 42"

y = re.findall("[0-9]+", x)     #X icindeki sayilari bana liste halinde yazdir anlamina gelir

print(y)

y = re.findall("[AEIOU]+", x)       #BÜYÜK HARF DIKKATE ALINARAK BU HARFLERDEN BIRISI VAR MI BAKAR
print(y)                #[] CIKTISINI VERIR


y = re.findall("[AEIOMU]+", x)          #EGER VARSA LISTE HALINDE SARTI SAGLAYAN HARFLERI YAZAR
print(y)            #['M'] CIKTISINI VERIR

