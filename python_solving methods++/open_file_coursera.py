#FORMAT ---> handle = open(filename,mode) 

fhand = open("/Users/dogukan/Desktop/python_kendi_calisma/python_Denemeler/romeo.txt", 'r')
print(fhand)
count = 0
for words in fhand :
    count += 1
    print(words)
    print(count)
    print(words[:10])



dosya = open("/Users/dogukan/Desktop/python_kendi_calisma/python_Denemeler/romeo.txt", 'r')
inp = dosya.read()      #!!!!TÜM SATIRLARI YAN YANA KOYAR.\n bir karakter olarak alir.
print(len(inp))
print(inp[:50])            #BURDA DA TEK SATIRDAYKEN DILIMLEME ILE ISTEDIGIMIZE KADAR ALABILIRZ
