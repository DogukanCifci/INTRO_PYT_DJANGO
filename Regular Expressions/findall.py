import re 
fhand = open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/Regular Expressions/mbox-short.txt", "r")

for lines in fhand :
    y = re.findall("^F.+:", lines)      #F ile baslayan ve devam eden cümleleri : a kadar al.
                                        #lines icinde : yoksa sarti saglamaz.Bos liste döndürür.
    print(y)                               #Ciktida gözüküyor + DEVAM ET ÖYLE DEMEK TA KI BIR SONRAKI SART OLARAK KOYDUGUMU SEYE KADAR

#######FINDALL LISTE DÖNDÜRÜR VE SARTI SAGLAYAN KELIMELERI DÖNDÜRÜR. 


