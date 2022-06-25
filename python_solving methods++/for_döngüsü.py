

for i in [1, 3, 6, 123, 5124, 1234, 7, 5] :
    print(i)

print("Finish")


# Yeni Liste

arkadaslar = ['Ali', 'Mehmet', 'Ömer', 'Tolga', 'Bedir', 'Iscan', 'Erol']
for friends in arkadaslar :
    print('Mutlu yillar:', friends)

print('Break')


#!!!!!!!!

bayram_liste = ['Ali', 'Kahraman', 'Solak', 'Mücahit']
for gelecekler in bayram_liste :
    print('Bayram aktivitesine gelecek kisiler:', gelecekler)

print('DONE!!')



###!!!!!!!

print('Baslama')
for i in [3, 7, 5, 'Ads', 324, 'adsa'] :
    print(i)

print('Son')


###!!!!!!!!

largest_so_far = -1
print('Ilk sayimiz:', largest_so_far)
for numbers in [1, 9, 41, 12, 3, 74, 15] :
    if numbers > largest_so_far :
        largest_so_far = numbers
    print('largest_so_far:', largest_so_far, 'numbers', numbers)

print('Listedeki en büyük sayi..:', largest_so_far)



#!!!!!!!!

sayac = 1
print('Before:', sayac)

for sayilar in [1, 8, 9, 25, 32, 44] :
    print(sayac, '...:', sayilar)
    sayac += 1
print('Done!!:', sayac)


print('SAYAC 0 DAN BASLATIP PRINTTEN ÖNCE YAZARSAK O ZAMAN SAYAC EN SON 6 OLARAK CIKAR YA DA EN SON PRINT(SAYAC-1) YAPMAK ZORUNDAYIZ')
sayac = 0
print('Before:', sayac)

for sayilar in [1, 8, 9, 25, 32, 44] :
    sayac += 1
    print(sayac, '...:', sayilar)
    
print('Done!!:', sayac)

#!!!!!!!!!
toplam = 0 
print('Baslangic=', toplam)

for the_numbers in [1, 7, 51, 9, 8,7, 17] :

    toplam += the_numbers
    print(toplam, 'and', the_numbers)

print("Icerdeki tüm sayilarin toplami =", toplam)

#          !!!!!! AVERAGE

toplam = 0 
print('Baslangic=', toplam)
sayac = 0
print("Sayac=", sayac)
for the_numbers in [1, 7, 51, 9, 8,7, 17] :
    sayac += 1
    toplam += the_numbers
    print(sayac,'-', toplam, 'and', the_numbers)

print("Icerdeki tüm sayilarin toplaminin ortalamasi =", toplam/sayac)


#!!!!!!!

deger = False   #3ü bulduktan sonra degeri trueya döndürcez
print('Before', deger)

for numbers in [1, 75, 23, 84, 3, 24, 123] :
    if numbers == 3 :
        deger = True
    
    print(deger, numbers)

print('After', deger)


#!!!!! En kücük degeri bulma

kücük = 100
print("Before =", kücük)
for numbers in [14, 78, 13, 4, 41, 36, 110] :           # Ama bu saglikli bir kod degil cünkü bütün sayilar 100 den büyük olursa listedeki en kücük sayiyi bulamayiz. sonucu bize 100 olarak verir.
    if numbers < kücük :
        kücük = numbers     
        print('Simdiye kadar ki en kücük sayi =', kücük)

print('Listedeki en kücük sayi =', kücük)


#Onun icin !!!!!!

min = None
print("Before =", min)

for number in [12, 412,64, 3, 6, 123, 74] :  
    if min == None :
        min = number
        print('Simdiye kadar ki en kücük sayimiz =', min)
        
    if number < min :
        min = number
        print('Simdiye kadar ki en kücük sayimiz =', min)

print('Listedeki en kücük sayimiz =', min)


   
