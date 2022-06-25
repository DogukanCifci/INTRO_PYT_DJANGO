from asyncio.base_futures import _FINISHED


n = 2
sonuc = 0
sayi = int(input("Bir sayi giriniz...."))

while n < sayi :
    sonuc = sayi % n
    if sonuc == 0 :
        print('Bu asal sayi degildir')
        break   
    else :
        n = n + 1 
        if n >= sayi :
            print('Girdiginiz sayi asal sayidir')

print('islem bitti')

        


