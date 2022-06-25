cümle = 'Mistakes are for the peoplrrrrrr'
print('liste else olmadan hali')
print(list(i for i in cümle if not i in 'aeuoi' )) 
print()

print('Set yani tekrar eden harflerle else komutu olmadan hali')   #list oldugu icin tekrar eden harfeleri de yazdirir
print(set(i for i in cümle if not i in 'aeuoi' ))       #set oldgu icin tekrar eden harfleri bir kere yazar
print()

print('SET komutu ve else komutu da var satirin icinde')   
print(set(i if not i in 'aeoui' else 10 for i in cümle)) #!!!EGER ELSE KOMUTUNU DA YAZACAKSAK FOR DÖNGÜSÜ EN SONA GIDER ÖNCE CONDITIONLAR YAZILIR
print()

print('list ile ve else ile yazilan')
print(list(i if not i in 'aeuoi' else 10 for i in cümle))