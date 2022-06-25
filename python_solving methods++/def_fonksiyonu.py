def ornek1() :
    print('Hello')
    print('def örnegini yaptik')   ### Asagidaki kodu yazana kadar bu kod beklemede kalir ve asagida fonksiyon ismini yazfdigimizda aktif hale gelir

ornek1()
print('aradaki diger cümle')
ornek1()


big = max('Merhaba ben buraya yeni tasindim')
print(big)

small = min('Buraya ne zaman tasindin?') #Bosluk en kücük olacagi icin ciktida bosluk gözükür fakat göremeyiz
print(small)

a = '123'

print(a, 1, end ='')

print()
print()
print()
def selamlama(dil) :
    if dil == 'de' :
        print('HALLO')
    
    elif dil == 'es' :
        print('HOLA')

    elif dil == 'tr' :
        print('MERHABA')
    
    else :
        print('HELLO')

print(input('Lütfen isminizi yaziniz'))

selamlama(input('Dilinizin kisaltilmis halini giriniz')) 


def ikili_girdi(x, y) :
    sonuc = x + y 
    return sonuc

a = ikili_girdi(5, 8)

print(a)

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)