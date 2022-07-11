fhand = open("/Users/dogukan/Desktop/Regular Expressions/mbox-short.txt", "r")

for lines in fhand :
    lines =lines.rstrip()
    if lines.startswith('From: ') :
        print(lines)



#Yerine 


import re 
hand = open("/Users/dogukan/Desktop/Regular Expressions/mbox-short.txt", "r")

for line in hand :
    line = line.rstrip()
    if re.search('^From: ', line) :         #Birinci yere sartimiz, ikinci yerede nerde aradigimizi yaziyoruz.
        print(line)



#######  ^ isareti startswith anlamina gelmekte


import re 
fhand = open("/Users/dogukan/Desktop/Regular Expressions/mbox-short.txt", "r")

for line in fhand :
    line = line.rstrip()
    if re.search("^X-\S+:", line) : 
        print(line)                     #\S bosluk olmayan herhangi birkarakter anlamina geliyor.
                                        #+ KENDINDEN BIR ÖNCEKI SARTI SAGLAYAN SEYLER ANLAMINA GELIYOR.
#YANI BUNUN ANLAMI X- ILE BASLA. DAHA SONRA BOSLUK OLMADAN DEVAM ET : KARAKTERI GELENE KADAR.
#CIKTIYA BAKARSA K: YA KADAR HICBIR BOSLUK YOK VE HEPSI X- ILE BASLAMISTIR
        