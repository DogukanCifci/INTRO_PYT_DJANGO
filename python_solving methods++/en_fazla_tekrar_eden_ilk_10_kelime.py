text = input('ENTER THE TEXT : ')
word_list = dict()
word_list2 = list()
kelimeler = text.split()
#------LISTENIN NASIL OLUSTUGU----------
for ii in kelimeler :
  word_list[ii] = word_list.get(ii, 0) + 1   #Bu metodun aciklamasi yukarda. kEY VE VALUE DEGERI ATAMA
  print(word_list)

print()
#---VALUE VE KEYS YER DEGISTIRDKTEN SONRA--------
for z, v in word_list.items() :
  word_list2.append((v,z))
print(word_list2)

print()
#---------------LISTENIN VALUELARA YANI TEKRAR SAYISINA GÖREN BÜYÜKTEN KÜCÜGE DOGRU SIRALANMIS HALI--------------
word_list2 = sorted(word_list2, reverse = True)
print(word_list2)

print()
print('------------------EN FAZLA TEKRAR EDEN 3LU-------------------')
print(word_list2[:3])

##COLAB CALISMASINDA VAR (BIR METIN ICINDE EN FAZLA TEKRAR EDEN ...)


#BUNDAN SONRASI ISTEGE BAGLI. DICTE CEVIRIP SADECE VALUES YXA DA KEYS LERI DÖNDÜREBILIRIZ.
# word_list2 = dict(word_list2)
# print(word_list2)
# print('KEYS-YANI TEKRAR SAYISI : ', word_list2.keys())
#print()
#print('MAX TEKRAR SAYISI = ', max(word_list2.keys()))