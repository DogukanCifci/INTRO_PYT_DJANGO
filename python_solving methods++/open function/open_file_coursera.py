#FORMAT ---> handle = open(filename,mode) 

fhand = open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/python_solving methods++/open function/romeo.txt", 'r')
print(fhand)
count = 0
for words in fhand :
    words = words.rstrip()
    count += 1
    print(count)
    print(words)
    print('*'*5)

    print(words[:10])
    print('-'*5)


dosya = open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/python_solving methods++/open function/romeo.txt", 'r')
inp = dosya.read()      #!!!!TÜM SATIRLARI YAN YANA KOYAR.\n bir karakter olarak alir.
print(len(inp))
print(inp[:50])            #BURDA DA TEK SATIRDAYKEN DILIMLEME ILE ISTEDIGIMIZE KADAR ALABILIRZ
