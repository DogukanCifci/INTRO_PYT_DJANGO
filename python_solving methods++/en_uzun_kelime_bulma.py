

####pythonic cözüm icin 
cumle = input("Give me a sentence..:")      #normalde calismasi gerekiyor. ayni kod baska yerde calisiyor. Pythonic cözüm
kelime = cumle.split()  #kelime listesi
enuzun = max(kelime, key=len)
print(f"En uzun kelime.:: {enuzun} ve karakter sayısı..:{len(enuzun)}")


########## Normal döngü ile cözüm

sentence = input('Enter a sentence')
sentence = list(sentence.split())
word = 0
max = 0
deger = None
while word < len(list(sentence))  :
  word += 1
  if len(sentence[word-1]) > max :
    max= len(sentence[word-1])
    deger = sentence[word-1]

print(f'En uzun kelime : {deger} \nKelime uzunlugu : {max}')


