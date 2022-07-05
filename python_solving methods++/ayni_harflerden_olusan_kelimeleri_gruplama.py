liste = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]

list2  =list()
for i in liste :
    list1 = list()          #list1 burda tanimlamimizin nedeni listeyi sifirlamak. Yoksa ilk döngüdeki kelimelere ekleyerek gider.
    for j in liste :
        if set(i) == set(j) :
            list1.append(j)
    print(list1)            #aralarda ne oldugunu görmek icin
    print()                 #aralarda ne oldugunu görmek icin
    if list1 not in list2 :
        list2.append(list1)
print('Sonuc------>', list2)