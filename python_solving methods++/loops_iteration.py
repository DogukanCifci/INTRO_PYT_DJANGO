

while True :
    line = input('Kelimeyi gir...:')

    if line[0] == '#' :   
        print('Kelimenin basina # isarei koymayin')      
        continue                                #continue komutu direk while basina geri döner

    if line == 'done' :                      #break komutu if komutunun altinda olsa  bile eger if komutu saglanirsa break otomatik olarak while kapatir!!!!!                                                                                        
        break                               #Döngü biz done yazana kadar devam eder
    print(line)

print('!!!!!Done!!!!!')

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff')


n= 0
while n <= 5 :
    print(n)
    n += 1

print('blastoff!')
print(n)