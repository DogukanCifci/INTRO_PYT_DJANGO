from importlib.machinery import SourceFileLoader            # Auf jeden Fall mus ich das schreiben


#Isim verirken cekecegim dosyainn ismini verdim !!!
#Asagida terminalde nerde oldgum gözüküyor. Ona göre bir path olusturarak eger iceri gireceksek ./ disari cikacaksak ../ ile LInuxdaki gibi path olusturacagiz ve dosyayi cekecegiz.

deneme1 = SourceFileLoader('deneme1', './Module-Package/my_package/deneme1.py').load_module()

japan = SourceFileLoader('asya', './Module-Package/my_package/my_subpack/asya/japan.py').load_module()

kore = SourceFileLoader('kore', './Module-Package/my_package/my_subpack/asya/kore.py').load_module()


print()
deneme1.deneme_func()           #Module-Pack icindeki my_package daki deneme1 dosyasinin icindeki deneme_func fonksiyonun cagirdik
print()
print(japan.karekök(18))        #Module-Pack icindeki my_package icindeki _my_subpack icindeki asya klasörünün icindeki japan dosyasindan karekök fonksiyonunu cagirdik
print()
kore.kore_func()                #Module-Pack icindeki my_package icindeki _my_subpack icindeki asya klasörünün icindeki kore dosyasindan kore_func fonksiyonunu cagirdik
