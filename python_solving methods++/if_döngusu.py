x = input('Bir sayi giriniz')

x = int(x)

if x < 2 :
    print("Smaller")

elif x < 10 :
    print("Medium")

else :
    print("Large")

print("ALL DONE")


girdi1 = 'Hello Bob'

try :
    girdi2 = int(girdi1)

except : 
    girdi2 = -3

print('Girilen sayi: ', girdi2)



a = '456'
try : 
    a = int(a)

except : 
    a = 1

print('Sayi Degeri:', a)


c = 'BOB'

try : 
    print(' Hello')
    b = int(c)      #Bu kisim calismayacagindan dolayi print('There') komutu da calismayacak ve direk except kismina gecicek
    print('There')

except :
    b = 4

print('Done', b)

a = input('Enter a number')

try : 
    girilen_sayi = int(a)
   
except : 
    girilen_sayi = -1

if girilen_sayi >= 0:
        print('Good Job')
    
else :
        print(girilen_sayi, 'is not a number')
        

