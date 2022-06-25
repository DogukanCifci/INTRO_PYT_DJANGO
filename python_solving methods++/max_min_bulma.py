smallest = None                     ####!!!!!!ÖNEMLI BIR ÖRNEK !!!!!!
largest = None

while True :
    girilen_sayi = input('BIR SAYI GIRINIZ')

    if girilen_sayi == "done" :
        break

    try :
        girilen_sayi = float(girilen_sayi)
    
    except :
        print('Invalid Input')
        continue
    
    if smallest == None :
        smallest = girilen_sayi 

    if largest == None :
        largest = girilen_sayi 
    
    if girilen_sayi > largest :
        largest = girilen_sayi 
    
    if girilen_sayi < smallest :
        smallest = girilen_sayi 

print('Girilem max sayi =', largest)
print('Girilen min sayi =', smallest)







