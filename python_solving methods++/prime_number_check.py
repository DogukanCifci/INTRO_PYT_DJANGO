sayi = input('Enter a number to chek if it is prime number : ')
count = 0
if sayi.isdigit() :
    sayi = int(sayi)
    for i in range(2, sayi) :
        if sayi % i == 0 :
            count += 1 
    if count > 0 :
        print(f'Number {sayi} is not a prime number')

    else :  
        print(f'Number {sayi} is a prime number')
else :
        print('The input is not a number')


