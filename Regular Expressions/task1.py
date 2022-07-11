import re 
x = """Neden program yazmayı öğrenmelisiniz? 7746
12 1929 8827
Program yazmak (veya programlamak) çok yaratıcı bir
7 ve ödüllendirici aktivite. programlar yazabilirsiniz
hayatını kazanmaktan çözmeye kadar birçok neden
8837 zor bir veri analizi problemine yardımcı olmak için eğlenmek için 128
başkası bir sorunu çözer. Bu kitap varsayar ki
herkes programlamayı bilmeli..."""
liste = list()

y = re.findall("[0-9]+", x)
toplam = 0
for i in range(len(y)) :
    a = float(y[i])
    toplam  += a

print("The sum of the numbers = ", toplam)


