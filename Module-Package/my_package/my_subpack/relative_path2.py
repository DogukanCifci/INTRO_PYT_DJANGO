from importlib.machinery import SourceFileLoader            # Auf jeden Fall mus ich das schreiben


#Isim verirken cekecegim dosyainn ismini verdim !!!
#Asagida terminalde nerde oldgum gözüküyor. Ona göre bir path olusturarak eger iceri gireceksek ./ disari cikacaksak ../ ile LInuxdaki gibi path olusturacagiz ve dosyayi cekecegiz.

deneme1 = SourceFileLoader('deneme1', './Module-Package/my_package/deneme1.py').load_module()

japan = SourceFileLoader('asya', './Module-Package/my_package/my_subpack/asya/japan.py').load_module()



deneme1.deneme_func()

print(japan.karekök(18))


