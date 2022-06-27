prime_sayilar = list()

while True : 
  numbers = (input('Enter a number : '))
  
  if numbers == 'done' :
    break 
  
  elif numbers.isdigit() :
    numbers = int(numbers)
    counter = 0
    for i in range(2,numbers) :
        if  numbers % i == 0 :
            counter += 1

    print('Counter : ', counter)
    print('sayi : ', numbers)
    if counter < 1 :
      prime_sayilar.append(numbers)
 
  else :
    print('Your entered is not valid!. Try Again')
    continue
if 1 in prime_sayilar :     #1 de asal sayi olmadigi icin eger en son varsa listeden cikartsin diye bu komutu yazdim.
    prime_sayilar.remove(1)

print(set(prime_sayilar))       #Ayni sayi birden fazla girildiyse ve asalsa sadece bir defa yazdirmak icin set yaptim.
#En basta listeye ekledim sonra en son set e cevirdim cünkü set append komutu almaz.